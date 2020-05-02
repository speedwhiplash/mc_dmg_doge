import { Injectable } from '@nestjs/common';
import { AllEquipment, BestOverallBuildFields, BobPostBodyType, BuildIndex, EquipmentFields } from '../interfaces';
import { Observable, of } from 'rxjs';

@Injectable()
export class CompareService {
	bestBuild: BuildIndex = {offhand: 0, chestplate: 0, leggings: 0, helmet: 0, boots: 0};
	bestScore = 10;
	idx = 0;

	bestOverallBuild(allEquipment: AllEquipment, bobStats: BobPostBodyType): Observable<BuildIndex> {
		console.time('build');

		let indexes: BuildIndex = {offhand: -1, chestplate: -1, leggings: -1, helmet: -1, boots: -1};
		this.deepCompare(allEquipment, indexes, 0, bobStats)
		console.log(`
	best score: ${this.bestScore}
	best build: 
	${allEquipment.boots[this.bestBuild.boots].Name}, 
	${allEquipment.chestplate[this.bestBuild.chestplate].Name},
	${allEquipment.helmet[this.bestBuild.helmet].Name},
	${allEquipment.leggings[this.bestBuild.leggings].Name},
	${allEquipment.offhand[this.bestBuild.offhand].Name}`
		);
		console.timeEnd('build');

		return of(<BuildIndex>{
			boots: this.bestBuild.boots,
			chestplate: this.bestBuild.chestplate,
			helmet: this.bestBuild.helmet,
			leggings: this.bestBuild.leggings,
			offhand: this.bestBuild.offhand
		});
	}

	private deepCompare(allEquipment: AllEquipment, indexes: BuildIndex, currentSlot, bobStats: BobPostBodyType): void {
		const slots = ['boots', 'chestplate', 'helmet', 'leggings', 'offhand'];
		let idx = 0;
		while (idx < allEquipment[slots[currentSlot]].length - 1) {
			if (currentSlot === 4) {
				const score = this.getScore(allEquipment, indexes, idx, bobStats);
				if (score < this.bestScore) {
					this.bestBuild = {
						boots: indexes[slots[0]],
						chestplate: indexes[slots[1]],
						helmet: indexes[slots[2]],
						leggings: indexes[slots[3]],
						offhand: idx
					};
					this.bestScore = score;
				}
			} else {
				indexes[slots[currentSlot]] = idx;
				this.deepCompare(allEquipment, indexes, currentSlot + 1, bobStats);
			}
			idx = idx + 1;
		}
	}

	private getScore(allEquipment: AllEquipment, indexes: BuildIndex, idx: number, bobStats: BobPostBodyType): number {
		let fields = {} as BestOverallBuildFields;
		[...Object.keys(bobStats.mainhand), 'Protection'].forEach(field => fields[field] = this.oneResult(allEquipment, indexes, idx, field));
		return this.applyRules(fields, bobStats);
	}

	private oneResult(allEquipment: AllEquipment, indexes: BuildIndex, idx: number, field: string): number {
		return allEquipment.boots[indexes.boots][field] +
			allEquipment.chestplate[indexes.chestplate][field] +
			allEquipment.helmet[indexes.helmet][field] +
			allEquipment.leggings[indexes.leggings][field] +
			allEquipment.offhand[idx][field]
	}

	private applyRules(fields: BestOverallBuildFields, bobStats: BobPostBodyType) {
		const resistance = bobStats.scenario['Damage Absorbed'];
		const armor = this.sum_stat_w_per(EquipmentFields.Armor, EquipmentFields['Armor Percent'], fields, bobStats.player, bobStats.mainhand);
		const toughness = this.sum_stat_w_per(EquipmentFields.Toughness, EquipmentFields['Toughness Percent'], fields, bobStats.player, bobStats.mainhand);
		const protection = +fields[EquipmentFields.Protection];
		const evasion = +fields[EquipmentFields.Evasion] + +bobStats.mainhand.Evasion;
		const regen = +fields[EquipmentFields.Regeneration] + +bobStats.mainhand.Regeneration;
		const health = this.sum_stat_w_per(EquipmentFields.Health, EquipmentFields['Health Percent'], fields, bobStats.player, bobStats.mainhand);

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

	private sum_stat_w_per(stat: EquipmentFields, percent: EquipmentFields, fields: BestOverallBuildFields, player_stats, mainhand_stats) {
		let statTotal = fields[<any>stat] +
			player_stats[stat] +
			mainhand_stats[stat];
		let statPercentTotal = (fields[<any>percent] +
			player_stats[percent] +
			mainhand_stats[percent]) / 100.0
		return statTotal * statPercentTotal;
	}
}
