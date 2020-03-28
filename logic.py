def one_result(list, slot_idxs, idx, stat):
    return [one_stat(list, 0, slot_idxs[0], stat),
            one_stat(list, 1, slot_idxs[1], stat),
            one_stat(list, 2, slot_idxs[2], stat),
            one_stat(list, 3, slot_idxs[3], stat),
            one_stat(list, 4, idx - 1, stat)]


def one_stat(list, slot_idx, iteration, stat):
    return list[slot_idx][iteration][stat]


"""
same as sum(values)
def add_stats(values):
    total = 0
    for val in values:
        total += val
    return(total)

same as max(values)
Max Fire Protection = max(Fire Protection)
Thorns              = max(Thorns)
"""


def create_slot_counters(list):
    slot_idxs = []
    values = []
    for i in range(len(list)):
        slot_idxs.append(-1)
        values.append(len(list[i]))
    return (slot_idxs, values)


def compare(list, slot_idxs, idx, stat, stats, player_stats, damage):
    stats_dict = {}
    stat_result = []
    for i in range(len(stats)):
        stat_result = one_result(list, slot_idxs, idx, stats[i])
        stats_dict.update({stats[i]: stat_result})
    to_check = compare_rules(stat, stats, stats_dict, player_stats, damage)
    return to_check


best = 0
best_idxs = []


def best_guess(guess):
    global best
    best = float(guess)


def is_last_slot(slot_idxs, a):
    return (len(slot_idxs) - 1) == a


def deep_compare(armor_slots_list, slot_idxs, values, current_slot, stat, stats, player_stats, how, damage):
    global best, best_idxs
    idx = 0
    while idx < values[current_slot]:
        if is_last_slot(slot_idxs, current_slot):
            to_check = compare(armor_slots_list, slot_idxs, idx, stat, stats, player_stats, damage)
            if min(best, to_check) != best:
                best = to_check
                best_idxs = [slot_idxs[0], slot_idxs[1], slot_idxs[2], slot_idxs[3], idx]
        else:
            slot_idxs[current_slot] = idx
            deep_compare(armor_slots_list, slot_idxs, values, current_slot + 1, stat, stats, player_stats, how, damage)

        idx = idx + 1


def get_best():
    global best_idxs
    return best_idxs


def evasion_reduction(evasion):
    if evasion >= 10:
        return 0.40
    elif evasion >= 20:
        return 0.80
    else:
        return 0


def armor_reduction(armor, toughness, damage):
    return 0.04 * min(20.0, max(armor / 5.0, armor - (damage / (2.0 + (toughness / 4.0)))))


def protection_reduction(protection):
    if protection < 20:
        return protection / 25.0
    elif protection >= 20:
        return 0.80


def second_wind(level):
    return level ** 0.5


def fire_duration(protection):
    return max(0, 1 - (0.15 * protection))


def reduced_damage(reduction):
    return 1 - reduction


def compare_rules(stat, stats, stats_dict, player_stats, damage):
    if stat == 'melee damage':
        armor = sum(stats_dict['Armor']) * (sum(stats_dict['Armor Percent']) + player_stats['Armor Percent']) / 100.0
        toughness = sum(stats_dict['Toughness']) * (sum(stats_dict['Toughness Percent']) + player_stats['Toughness Percent']) / 100.0
        health = (sum(stats_dict['Health']) + player_stats['Health']) * (sum(stats_dict['Health Percent']) + player_stats['Health Percent']) / 100.0
        evasion_reduced = damage * reduced_damage(evasion_reduction(sum(stats_dict['Evasion'])))
        melee_damage = (evasion_reduced * reduced_damage(armor_reduction(armor, toughness, evasion_reduced)) * reduced_damage(protection_reduction(sum(stats_dict['Protection']))) + second_wind(sum(stats_dict['Second Wind']))) / health
        return melee_damage
    else:
        return 1000
