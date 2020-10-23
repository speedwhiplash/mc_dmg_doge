import { BuildAttributesScore, Dictionary, IBobInputs } from '../../../interfaces';
import { armor_reduction, evasion_reduction, life_drain, protection_reduction, reduced_damage, regeneration } from '../../compare-util';

export const totalDefenseScore = (fieldScore: Dictionary<number>, bobStats: IBobInputs): BuildAttributesScore => {
	const resistance = bobStats.scenario['Damage Absorbed'] / 100;
	const armor = fieldScore.Armor * fieldScore['Armor Percent'] / 100;
	const toughness = fieldScore.Toughness * fieldScore['Toughness Percent'] / 100;
	const protection = fieldScore.Protection;
	const evasion = fieldScore.Evasion;
	const health = Math.max(0, fieldScore.Health * fieldScore['Health Percent'] / 100);
	const base_attack_speed = bobStats.mainhand['Attack Speed'];
	const attack_speed = fieldScore['Attack Speed'] * fieldScore['Attack Speed Percent'] / 100;
	const crit_chance = bobStats.scenario['Crit Chance'] / 100;
	const speed_percent = fieldScore.Speed * fieldScore['Speed Percent'] / 10;
	const anemia = fieldScore.Anemia;
	const sustenance = fieldScore.Sustenance;
	const corruption = fieldScore.Corruption;

	const worst_melee_reduced = bobStats.scenario.Damage * reduced_damage(evasion_reduction(evasion));
	const worst_melee_damage = bobStats.scenario['Hits Taken'] * (worst_melee_reduced * reduced_damage(armor_reduction(armor, toughness, worst_melee_reduced)) * reduced_damage(protection_reduction(protection)) * resistance);
	const worst_injury_score = worst_melee_damage / health;

	const best_melee_reduced = bobStats.scenario.Damage * reduced_damage(evasion_reduction(evasion + 5));
	const best_melee_damage = bobStats.scenario['Hits Taken'] * (best_melee_reduced * reduced_damage(armor_reduction(armor, toughness, best_melee_reduced)) * reduced_damage(protection_reduction(protection)) * resistance);

	let score = 1;

	if (
		(speed_percent >= (bobStats.scenario['Minimum Speed'] / 100)) &&
		(worst_injury_score < 1) &&
		(corruption <= 1)
	) {
		const regen_gain = regeneration(fieldScore.Regeneration);
		const life_drain_gain = life_drain(fieldScore['Life Drain'], base_attack_speed, attack_speed, crit_chance)
		const other_gain = bobStats.scenario['Health Regained'];
		const health_gain = (1 - (0.1 * anemia)) * (1 + (0.1 * sustenance)) * (regen_gain + life_drain_gain + other_gain);
		const average_melee_damage = worst_melee_damage + ((0.2 * (evasion % 5)) * (best_melee_damage - worst_melee_damage));
		const percent_score = (average_melee_damage - health_gain) / health;

		score = percent_score - (bobStats.scenario['Health Regain Percent'] / 100);
	}

	return {armor, toughness, protection, evasion, regeneration: fieldScore.Regeneration, health, speed_percent, score};
}
