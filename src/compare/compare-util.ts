import { AllEquipment, BuildAttributeScores, IBuild } from '../interfaces';

export const oneResult = (build: IBuild, field: string): number => {
	return (build.helmet[field] || 0) +
		(build.chestplate[field] || 0) +
		(build.leggings[field] || 0) +
		(build.boots[field] || 0) +
		(build.offhand[field] || 0) +
		(build.player[field] || 0) +
		(build.mainhand[field] || 0);
}

export const transformIndexesIntoNames = (scores: BuildAttributeScores, equipment: AllEquipment): BuildAttributeScores => {
	const scoreKeys = Object.keys(scores);
	let namedScores: BuildAttributeScores = {};
	scoreKeys.forEach(scoreKey => {
		namedScores[scoreKey] = [];
		scores[scoreKey].forEach(item => {
			namedScores[scoreKey].push({
				build: {
					helmet: equipment.helmet[item.build.helmet].Name,
					chestplate: equipment.chestplate[item.build.chestplate].Name,
					leggings: equipment.leggings[item.build.leggings].Name,
					boots: equipment.boots[item.build.boots].Name,
					offhand: equipment.offhand[item.build.offhand].Name,
				},
				scores: { ...item.scores }
			})
		})
	})
	return namedScores;
}

export const armor_reduction = (armor, toughness, damage) => {
	const capped_armor = Math.min(30.0, Math.max(0, armor));
	const capped_toughness = Math.min(20.0, Math.max(0, toughness));

	return 0.04 * Math.min(20.0, Math.max(capped_armor / 5.0, capped_armor - (damage / (2.0 + (capped_toughness / 4.0)))));
}

export const evasion_reduction = (evasion) => {
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

export const life_drain = (level, base_attack_speed, attack_speed, crit_chance) => {
	if (base_attack_speed == 0) {
		return 0;
	} else {
		const attack_speed_capped = Math.min(2, attack_speed);
		const attacks = Math.floor((2 / Math.ceil(2 / attack_speed_capped)) + 1);

		const life_drain_heal_crit = crit_chance * Math.sqrt(level);
		const life_drain_heal = 0.5 * (1 - crit_chance) * Math.sqrt(level) / Math.sqrt(base_attack_speed);

		return attacks * (life_drain_heal_crit + life_drain_heal);
	}
}

export const protection_reduction = (protection): number => {
	return protection < 20 ? (protection / 25.0) : 0.80;
}

export const reduced_damage = (reduction = 0) => {
	return 1 - reduction;
}

export const regeneration = (level) => {
	return Math.sqrt(level);
}
