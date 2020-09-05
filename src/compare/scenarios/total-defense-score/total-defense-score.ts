import { BuildAttributesScore, Dictionary, IBobInputs } from '../../../interfaces';
import { armor_reduction, evasion_reduction, life_drain, protection_reduction, reduced_damage, regeneration } from '../../compare-util';

export const totalDefenseScore = (fieldScore: Dictionary<number>, bobStats: IBobInputs): BuildAttributesScore => {
	const resistance = bobStats.scenario['Damage Absorbed'] / 100;
	const armor = fieldScore.Armor * fieldScore['Armor Percent'] / 100;
	const toughness = fieldScore.Toughness * fieldScore['Toughness Percent'] / 100;
	const protection = fieldScore.Protection;
	const evasion = fieldScore.Evasion;
	const health = fieldScore.Health * fieldScore['Health Percent'] / 100;
	const base_attack_speed = bobStats.mainhand['Attack Speed'];
	const attack_speed = fieldScore['Attack Speed'] * fieldScore['Attack Speed Percent'] / 100;
	const crit_chance = bobStats.scenario['Crit Chance'] / 100;
	const speed_percent = fieldScore.Speed * fieldScore['Speed Percent'] / 10;
	const anemia = fieldScore.Anemia;
	const corruption = fieldScore.Corruption;

	const melee_reduced = bobStats.scenario.Damage * reduced_damage(evasion_reduction(evasion));
	const melee_damage = bobStats.scenario['Hits Taken'] * (melee_reduced * reduced_damage(armor_reduction(armor, toughness, melee_reduced)) * reduced_damage(protection_reduction(protection)) * resistance);
	const injury_score = melee_damage / health;

	let score = 1;

	if ((injury_score < 1) && (speed_percent >= (bobStats.scenario['Minimum Speed'] / 100)) && (corruption <= 1)) {
		const regen_gain = (1 - (0.1 * anemia)) * regeneration(fieldScore.Regeneration);
		const life_drain_gain = (1 - (0.1 * anemia)) * life_drain(fieldScore['Life Drain'], base_attack_speed, attack_speed, crit_chance)
		const other_gain = (1 - (0.1 * anemia)) * bobStats.scenario['Health Regained'];
		const health_gain = regen_gain + life_drain_gain + other_gain;
		const percent_score = (melee_damage - health_gain) / health;

		score = percent_score - (bobStats.scenario['Health Regain Percent'] / 100);
	}

	return {armor, toughness, protection, evasion, regeneration: fieldScore.Regeneration, health, speed_percent, score};
}
