
def one_result(list, slot_idxs, idx, stat):
    return[one_stat(list, 0, slot_idxs[0], stat),
           one_stat(list, 1, slot_idxs[1], stat),
           one_stat(list, 2, slot_idxs[2], stat),
           one_stat(list, 3, slot_idxs[3], stat),
           one_stat(list, 4, idx - 1, stat)]

def one_stat(list, slot_idx, iteration, stat):
	return(list[slot_idx].get('data')[iteration][stat])

# same as sum(values)
# def add_stats(values):
# 	total = 0
#     for val in values:
#         total += val
#     return(total)
#
# same as max(values)
# Max Fire Protection = max(Fire Protection)
# Thorns              = max(Thorns)

def create_slot_counters(list):
	slot_idxs = []
	values    = []
	for i in range(len(list)):
		slot_idxs.append(-1)
		values.append(len(list[i].get('data')))
	return(slot_idxs, values)

def compare(list, slot_idxs, idx, stat, stats, player_stats, damage):
	stats_dict = {}
	stat_result = []
	for i in range(len(stats)):
		stat_result = one_result(list, slot_idxs, idx, stats[i])
		stats_dict.update({stats[i] : stat_result})
	to_check = compare_rules(stat, stats, stats_dict, player_stats, damage)
	return(to_check)

def deep_compare(list, slot_idxs, values, current_slot, stat, stats, player_stats, how, guess, damage):
	idx = 0
	best = float(guess)
	best_idxs = []
	best_stats = []
	is_last_slot = lambda a : (len(slot_idxs) - 1) == a
	while idx < values[current_slot]:
		if is_last_slot(current_slot):
			to_check = compare(list, slot_idxs, idx, stat, stats, player_stats, damage)
			if min(best, to_check) != best:
				best = to_check
				best_idxs.append(idx)
				best_stats.append(best)
		else:
			slot_idxs[current_slot] = idx
			deep_compare(list, slot_idxs, values, current_slot + 1, stat, stats, player_stats, how, guess, damage)

		idx = idx + 1
	return(best_idxs, best_stats)

def evasion_reduction(evasion):
	if evasion >= 10:
		return(0.40)
	elif evasion >= 20:
		return(0.80)
	else:
		return(0)

def armor_reduction(armor, toughness, damage):
	return(0.04*min(20.0,max(armor/5.0,armor-(damage/(2.0 + (toughness/4.0))))))

def protection_reduction(protection):
	if protection < 20:
		return(protection/25.0)
	elif protection >= 20:
		return(0.80)

def second_wind(level):
	return(level**0.5)

def fire_duration(protection):
	return(max(0,1-(0.15*protection)))

def reduced_damage(reduction):
	return(1-reduction)

def compare_rules(stat, stats, stats_dict, player_stats, damage):
	if stat == 'melee damage':
		armor = sum(stats_dict['Armor'])*(sum(stats_dict['Armor Percent']) + player_stats['Armor Percent'])/100.0
		toughness = sum(stats_dict['Toughness'])*(sum(stats_dict['Toughness Percent']) + player_stats['Toughness Percent'])/100.0
		health = (sum(stats_dict['Health']) + player_stats['Health'])*(sum(stats_dict['Health Percent']) + player_stats['Health Percent'])/100.0
		evasion_reduced = damage*reduced_damage(evasion_reduction(sum(stats_dict['Evasion'])))
		melee_damage = (evasion_reduced*reduced_damage(armor_reduction(armor, toughness, evasion_reduced))*reduced_damage(protection_reduction(sum(stats_dict['Protection']))) + second_wind(sum(stats_dict['Second Wind'])))/health
		return(melee_damage)
	else:
		return(1000)

# for i in range(20):
# 	for j in range(17):
# 		for k in range(14):
# 			for m in range(14):
# 				for n in range(23):
# 					helmet(i)
# 					chestplate(j)
# 					pants(k)
# 					boots(m)
# 					hand(n)
# 					total_armor,total_speed_per,total_health,total_atk,total_bow_atk,abs_dmg_taken,per_dmg_taken = totals()
# 					if abs_dmg_taken < least_dmg_taken:
# 						least_dmg_taken = abs_dmg_taken
# 						least_per_dmg_taken = per_dmg_taken
# 						indices_of_best = [i,j,k,m,n]
# 						best_prot        = prot
# 						best_armor       = total_armor
# 						best_toughness   = toughness
# 						best_evasion     = evasion
# 						best_speed_per   = total_speed_per
# 						best_health      = total_health
# 						best_atk         = total_atk
# 						best_atk_spd_per = atk_spd_per
# 						best_bow_atk     = total_bow_atk
# 						best_arw_spd_per = arw_spd_per
# 						best_helm_name   = helm_name
# 						best_chest_name  = chest_name
# 						best_pants_name  = pants_name
# 						best_boots_name  = boots_name
# 						best_hand_name   = hand_name
