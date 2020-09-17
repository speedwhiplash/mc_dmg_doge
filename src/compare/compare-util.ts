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

export const reduced_damage = (reduction = 0) => {
	return 1 - reduction;
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

export const melee_evasion_reduction = (evasion, melee_evasion) => {
    return evasion_reduction(evasion + 2*melee_evasion);
}

export const ability_evasion_reduction = (evasion, ability_evasion) => {
    return evasion_reduction(evasion + 2*ability_evasion);
}

export const armor_reduction = (armor, toughness, damage) => {
	const capped_armor = Math.min(30.0, Math.max(0, armor));
	const capped_toughness = Math.min(20.0, Math.max(0, toughness));

	return 0.04 * Math.min(20.0, Math.max(capped_armor / 5.0, capped_armor - (damage / (2.0 + (capped_toughness / 4.0)))));
}

export const protection_reduction = (protection): number => {
	return protection < 20 ? (protection / 25.0) : 0.80;
}

export const fire_protection_reduction = (protection, fire_protection) => {
    return protection_reduction(protection + 2*fire_protection);
}

export const burn_time_multiplier = (max_fire_protection) => {
    return max_fire_protection < 6 ? (1 - (0.15 * max_fire_protection)) : 0;
}

export const blast_protection_reduction = (protection, blast_protection) => {
    return protection_reduction(protection + 2*blast_protection);
}

export const explosion_damage = (power, distance, exposure) => {
    const blast_radius = 0.3 * Math.floor(1.3 * power / 0.225);

    if (distance > 2*power) {
        return 0;
    } else {
        const impact = (1 - (distance / blast_radius)) * exposure;
        return Math.floor((((impact ** 2) + impact) * 7 * power) + 1);
    }
}

export const projectile_protection_reduction = (protection, projectile_protection) => {
    return protection_reduction(protection + 2*projectile_protection);
}

export const feather_falling_protection_reduction = (protection, feather_falling_protection) => {
    return protection_reduction(protection + 3*feather_falling_protection);
}

export const fall_damage = (distance) => {
	return distance > 3 ? (distance - 3) : 0;
}

export const regeneration = (level) => {
	return Math.sqrt(level);
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

export const health_gain = (regeneration_level, life_drain_level, base_attack_speed, attack_speed, crit_chance, health_gain, anemia) => {
    const regen_gain = regeneration(regeneration_level);
    const life_drain_gain = life_drain(life_drain_level, base_attack_speed, attack_speed, crit_chance)
    
    return (1 - (0.1 * anemia)) * (regen_gain + life_drain_gain + health_gain);
}