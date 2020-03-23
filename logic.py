from itertools import product
from data import armor_stats
from data import player_stats

def total(base, added, base_percent, added_percent):
	return((base + added)*(base_percent + added_percent))

def evasion_reduction():
	if evasion >= 10:
		return(0.40)
	elif evasion >= 20:
		return(0.80)

def armor_reduction():
	return(0.04*min(20.0,max(armor/5.0,armor-(damage/(2.0 + (toughness/4.0))))))

def protection_reduction(protection):
	if protection < 20:
		return(prot/25.0)
	elif protection >= 20:
		return(0.80)

def fire_duration(protection):
	return(1-(0.15*protection))

def reduced_damage(reduction):
	return(1-reduction)

def combinations(dictionary):
	return(list(product(*(dictionary[key] for key in dictionary))))

def compare_the_things(idx):
    current_slots = [
        all_the_things[0].get('data')[slot_idxs[0]][stat_to_compare],
        all_the_things[1].get('data')[slot_idxs[1]][stat_to_compare],
        all_the_things[2].get('data')[slot_idxs[2]][stat_to_compare],
        all_the_things[3].get('data')[slot_idxs[3]][stat_to_compare],
        all_the_things[4].get('data')[idx - 1][stat_to_compare]
    ]
    total_stat = 0
    for val in current_slots:
        total_stat = total_stat + val
    if (best_stats.get(stat_to_compare) is None) or total_stat > best_stats.get(stat_to_compare):
        best_stats[stat_to_compare] = total_stat
        print(total_stat, all_the_things[0].get('data')[slot_idxs[0]].get('Helmet Name'), all_the_things[4].get('data')[slot_idxs[4]].get('Offhand Name'))

# eMax = 0
# allTHEThings = armor_stats()
# print(allTHEThings['helmets'][0].get('Ethereal'))
#
# for i in range(len(allTHEThings['helmets'])):
#     eMax = max(eMax, allTHEThings['helmets'][i]['Ethereal'])
#
# print('eMax', eMax)

stat_to_compare = 'Ethereal'
best_idxs = []
best_stats = {}
slot_idxs = []
slot_counts = []
all_the_things = armor_stats()
for i in range(len(all_the_things)):
    slot_idxs.append(-1)
    slot_counts.append(len(all_the_things[i]['data']))

is_last_slot = lambda a : (len(slot_idxs) - 1) == a

def deep_compare(data, slot_idxs, curr_slot):
    idx = 0
    while idx < slot_counts[curr_slot]:
        if is_last_slot(curr_slot):
            compare_the_things(idx)
        else:
            slot_idxs[curr_slot] = idx
            deep_compare(data, slot_idxs, curr_slot + 1)

        idx = idx + 1

deep_compare(armor_stats(), slot_idxs, 0)
print(best_stats)

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
