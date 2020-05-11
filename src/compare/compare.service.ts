import { Injectable } from '@nestjs/common';
import { AllEquipment, BuildIndex, HandheldFields, IBobInputs, IBuild } from '../interfaces';
import { Observable, of } from 'rxjs';

export interface BuildScores {
	[key: number]: BuildIndex[]
}

interface ScorePerField {
	[key: string]: number
}

@Injectable()
export class CompareService {
	readonly TOP_NUM_OF_SCORES = 10;
	bestScore = 9;
	bestScores: BuildScores = {};
	worstBestScore = 10;

	bobDefense(allEquipment: AllEquipment, bobStats: IBobInputs): Observable<BuildScores> {
		console.time('build');
		this.resetScores();

		let indexes: BuildIndex = {helmet: -1, chestplate: -1, leggings: -1, boots: -1, offhand: -1};
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
	${allEquipment.boots[scores[bestIdx][0].boots].Name}, 
	${allEquipment.chestplate[scores[bestIdx][0].chestplate].Name},
	${allEquipment.helmet[scores[bestIdx][0].helmet].Name},
	${allEquipment.leggings[scores[bestIdx][0].leggings].Name},
	${allEquipment.offhand[scores[bestIdx][0].offhand].Name}`
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
				this.logScore(this.getScore(build, bobStats), {...indexes, offhand: idx});
			} else {
				indexes[slots[currentSlot]] = idx;
				this.deepCompare(allEquipment, indexes, currentSlot + 1, bobStats);
			}
			idx = idx + 1;
		}
	}

	private getScore(build: IBuild, bobStats): number {
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

	private totalDefenseScore(fieldScore: ScorePerField, bobStats) {
		const resistance = bobStats.scenario['Damage Absorbed'];
		const armor = fieldScore.Armor * fieldScore['Armor Percent'] / 100;
		const toughness = fieldScore.Toughness * fieldScore['Toughness Percent'] / 100;
		const protection = fieldScore.Protection;
		const evasion = fieldScore.Evasion;
		const regen = fieldScore.Regeneration;
		const health = fieldScore.Health * fieldScore['Health Percent'] / 100;

		const melee_reduced = bobStats.scenario.Damage * this.reduced_damage(this.evasion_reduction(evasion)) * (resistance / 100);
		const melee_damage = bobStats.scenario['Hits Taken'] * (melee_reduced * this.reduced_damage(this.armor_reduction(armor, toughness, melee_reduced)) * this.reduced_damage(this.protection_reduction(protection)));
		return (melee_damage - this.regeneration(regen, melee_damage)) / health;
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

	private regeneration(level, damage) {
		const amount = Math.sqrt(level);
		return damage > amount ? amount : damage;
	}

	private resetScores() {
		this.bestScore = 10;
		this.bestScores = {};
		this.worstBestScore = 9;
	}

	private logScore(score: number, indexes: BuildIndex) {
		if (score < this.worstBestScore) {
			this.bestScores[score] = [...(this.bestScores[score] || []), indexes];
			let scores = Object.keys(this.bestScores).map(score => +score).sort();
			if (scores.length > this.TOP_NUM_OF_SCORES) {
				delete this.bestScores[scores[this.TOP_NUM_OF_SCORES]];
			}
			this.worstBestScore = scores[scores.length - 1];
			this.bestScore = scores[0];
			console.log('worst best', this.worstBestScore);
			console.log('best', this.bestScore);
		}
	}
}
