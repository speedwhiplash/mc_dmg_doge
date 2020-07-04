import { Injectable } from '@nestjs/common';
import { AllEquipment, BuildIndex, BuildScores, DefenseScores, HandheldFields, IBobInputs, IBuild } from '../interfaces';
import { Observable, of } from 'rxjs';

interface ScorePerField {
	[key: string]: number;
}

const TOP_NUM_OF_SCORES = 15;
const PLAYER_REFLEX_DELAY = 0.2;

@Injectable()
export class CompareService {
	bestScore = 9;
	bestScores: BuildScores = {};
	worstBestScore = 10;
	numScores = 0;

	bobDefense(allEquipment: AllEquipment, bobStats: IBobInputs): Observable<BuildScores> {
		console.time('build');
		this.resetScores();

		let indexes: BuildIndex = { helmet: -1, chestplate: -1, leggings: -1, boots: -1, offhand: -1 };
		this.deepCompare(allEquipment, indexes, 0, bobStats);

		this.logBuildScore(this.bestScores, allEquipment);
		console.timeEnd('build');

		return of(this.bestScores);
	}

	private logBuildScore(scores: BuildScores, allEquipment: AllEquipment) {
		const scoreIndexes = Object.keys(scores).map(score => +score).sort();
		const bestIdx = scoreIndexes[0];
		console.log('bestIdx', bestIdx, scoreIndexes)
		console.log(`
	best score: ${bestIdx}
	best build: 
	${allEquipment.boots[scores[bestIdx][0].build.boots].Name}, 
	${allEquipment.chestplate[scores[bestIdx][0].build.chestplate].Name},
	${allEquipment.helmet[scores[bestIdx][0].build.helmet].Name},
	${allEquipment.leggings[scores[bestIdx][0].build.leggings].Name},
	${allEquipment.offhand[scores[bestIdx][0].build.offhand].Name}`
		);
	}

	private deepCompare(allEquipment: AllEquipment, indexes: BuildIndex, currentSlot, bobStats: IBobInputs): void {
		const slots = ['helmet', 'chestplate', 'leggings', 'boots', 'offhand'];
		let idx = 0;
		while (idx < allEquipment[slots[currentSlot]].length) {
			if (currentSlot === 4) {
				let build = {
					boots: allEquipment.boots[indexes.boots],
					chestplate: allEquipment.chestplate[indexes.chestplate],
					helmet: allEquipment.helmet[indexes.helmet],
					leggings: allEquipment.leggings[indexes.leggings],
					offhand: allEquipment.offhand[idx],
					player: bobStats.player,
					mainhand: bobStats.mainhand
				}
				this.recordBestScores(this.getScore(build, bobStats), { ...indexes, offhand: idx });
			} else {
				indexes[slots[currentSlot]] = idx;
				this.deepCompare(allEquipment, indexes, currentSlot + 1, bobStats);
			}
			idx = idx + 1;
		}
	}

	private getScore(build: IBuild, bobStats): DefenseScores {
		let fields = [...Object.keys(HandheldFields), 'Protection'];
		let fieldScore: ScorePerField = {};

		fields.forEach(field => fieldScore[field] = this.oneResult(build, field));
		return this.totalDefenseScore(fieldScore, bobStats);
	}

	private oneResult(build: IBuild, field: string): number {
		return (build.helmet[field] || 0) +
			(build.chestplate[field] || 0) +
			(build.leggings[field] || 0) +
			(build.boots[field] || 0) +
			(build.offhand[field] || 0) +
			(build.player[field] || 0) +
			(build.mainhand[field] || 0);
	}

	private totalDefenseScore(fieldScore: ScorePerField, bobStats): DefenseScores {
		const resistance = bobStats.scenario['Damage Absorbed'] / 100;
		const armor = fieldScore.Armor * fieldScore['Armor Percent'] / 100;
		const toughness = fieldScore.Toughness * fieldScore['Toughness Percent'] / 100;
		const protection = fieldScore.Protection;
		const evasion = fieldScore.Evasion;
		const regeneration = fieldScore.Regeneration;
		const life_drain = fieldScore['Life Drain'];
		const health = fieldScore.Health * fieldScore['Health Percent'] / 100;
		const attack_speed = fieldScore['Attack Speed'] * fieldScore['Attack Speed Percent'] / 100;
		const crit_chance = bobStats.scenario['Crit Chance'] / 100;

		const melee_reduced = bobStats.scenario.Damage * this.reduced_damage(this.evasion_reduction(evasion));
		const melee_damage = bobStats.scenario['Hits Taken'] * (melee_reduced * this.reduced_damage(this.armor_reduction(armor, toughness, melee_reduced)) * this.reduced_damage(this.protection_reduction(protection)) * resistance);
		const injury_score = melee_damage / health;
		let score = 1;
		if (injury_score < 1) {
			const percent_score = (melee_damage - this.regeneration(regeneration) - this.life_drain(life_drain, attack_speed, crit_chance) - bobStats.scenario['Health Regained']) / health;
			score = percent_score - (bobStats.scenario['Health Regain Percent'] / 100);
		}
		return { armor, toughness, protection, evasion, regeneration, health, score };
	}

	private armor_reduction(armor, toughness, damage) {
		return 0.04 * Math.min(20.0, Math.max(armor / 5.0, armor - (damage / (2.0 + (toughness / 4.0)))));
	}

	private evasion_reduction(evasion) {
		if (evasion >= 5 && evasion < 10) {
			return 0.20;
		} else if (evasion >= 10 && evasion < 15) {
			return 0.40;
		} else if (evasion >= 15 && evasion < 20) {
			return 0.60;
		} else if (evasion >= 20) {
			return 0.80;
		} else {
			return 0;
		}
	}

	private protection_reduction(protection): number {
		return protection < 20 ? (protection / 25.0) : 0.80;
	}

	private reduced_damage(reduction = 0) {
		return 1 - reduction;
	}

	private regeneration(level) {
		return Math.floor(Math.sqrt(level));
	}

	private life_drain(level, attack_speed, crit_chance) {
		if (attack_speed == 0) {
			return 0;
		} else { 
			const attack_speed_delayed = Math.min(2, 1 / ((1 / attack_speed) + PLAYER_REFLEX_DELAY));
            const attacks = Math.floor((1 / (0.5 * Math.ceil((1 / attack_speed_delayed) / 0.5))) + 1);

			const life_drain_heal_crit = crit_chance * Math.sqrt(level);
			const life_drain_heal = 0.25 * (1 - crit_chance) * Math.sqrt(level);
			
			return attacks * (life_drain_heal_crit + life_drain_heal);
		}
	}

	private resetScores() {
		this.bestScore = 10;
		this.bestScores = {};
		this.numScores = 0;
		this.worstBestScore = 9;
	}

	private recordBestScores(defenseScores: DefenseScores, indexes: BuildIndex) {
		if (this.numScores > TOP_NUM_OF_SCORES || defenseScores.score < this.worstBestScore) {
			// Allow multiple builds for same score
			this.bestScores[defenseScores.score] = [...(this.bestScores[defenseScores.score] || []), { build: indexes, scores: defenseScores }];

			let scores = Object.keys(this.bestScores).map(score => +score).sort();
			delete this.bestScores[scores[TOP_NUM_OF_SCORES]];
			this.worstBestScore = scores[scores.length - 1];
			this.bestScore = scores[0];

		}
	}
}
