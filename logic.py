def one_result(list, slot_idxs, idx, stat):
    return [one_stat(list, 0, slot_idxs[0], stat),
            one_stat(list, 1, slot_idxs[1], stat),
            one_stat(list, 2, slot_idxs[2], stat),
            one_stat(list, 3, slot_idxs[3], stat),
            one_stat(list, 4, idx - 1, stat)]


def one_stat(list, slot_idx, iteration, stat):
    return list[slot_idx][iteration][stat]


def create_slot_counters(list):
    slot_idxs = []
    values = []
    for i in range(len(list)):
        slot_idxs.append(-1)
        values.append(len(list[i]))
    return slot_idxs, values


def compare(list, slot_idxs, idx, stats, player_stats, damage, hits):
    stats_dict = {
        'Armor': one_result(list, slot_idxs, idx, 'Armor'),
        'Armor Percent': one_result(list, slot_idxs, idx, 'Armor Percent'),
        'Toughness': one_result(list, slot_idxs, idx, 'Toughness'),
        'Toughness Percent': one_result(list, slot_idxs, idx, 'Toughness Percent'),
        'Protection': one_result(list, slot_idxs, idx, 'Protection'),
        'Health': one_result(list, slot_idxs, idx, 'Health'),
        'Health Percent': one_result(list, slot_idxs, idx, 'Health Percent'),
        'Evasion': one_result(list, slot_idxs, idx, 'Evasion'),
        'Regeneration': one_result(list, slot_idxs, idx, 'Regeneration'),
    }
    to_check = compare_rules(stats, stats_dict, player_stats, damage, hits)
    return to_check


best = 1000
best_idxs = []

def is_last_slot(slot_idxs, a):
    return ((len(slot_idxs) - 1) == a)


def deep_compare(armor_slots_list, slot_idxs, values, current_slot, stats, player_stats, damage, hits):
    global best, best_idxs
    idx = 0
    while idx < values[current_slot]:
        if is_last_slot(slot_idxs, current_slot):
            to_check = compare(armor_slots_list, slot_idxs, idx, stats, player_stats, damage, hits)
            if to_check < best:
                best = to_check
                best_idxs = [slot_idxs[0], slot_idxs[1], slot_idxs[2], slot_idxs[3], idx]
        else:
            slot_idxs[current_slot] = idx
            deep_compare(armor_slots_list, slot_idxs, values, current_slot + 1, stats, player_stats, damage, hits)

        idx = idx + 1


def get_best():
    global best_idxs
    return best_idxs


def sum_stat_w_per(stat, percent, stats_dict, player_stats):
    return (sum(stats_dict[stat]) + player_stats[stat]) * (sum(stats_dict[percent]) + player_stats[percent]) / 100.0


def sum_stat(stat, stats_dict, player_stats):
    return sum(stats_dict[stat]) + player_stats[stat]


def evasion_reduction(evasion):
    if evasion >= 5 and evasion < 10:
        return (0.20)
    elif evasion >= 10 and evasion < 15:
        return (0.40)
    elif evasion >= 15 and evasion < 20:
        return (0.60)
    elif evasion >= 20:
        return (0.80)
    else:
        return (0)


def armor_reduction(armor, toughness, damage):
    return 0.04 * min(20.0, max(armor / 5.0, armor - (damage / (2.0 + (toughness / 4.0)))))


def protection_reduction(protection):
    if protection < 20:
        return protection / 25.0
    elif protection >= 20:
        return 0.80


def regeneration(level, damage):
    amount = level ** 0.5
    if damage >= amount:
        return amount
    else:
        return damage


def reduced_damage(reduction):
    return 1 - reduction


def compare_rules(stats, stats_dict, player_stats, damage, hits):
    resistance = player_stats['Damage Absorbed']
    armor = sum_stat_w_per('Armor', 'Armor Percent', stats_dict, player_stats)
    toughness = sum_stat_w_per('Toughness', 'Toughness Percent', stats_dict, player_stats)
    protection = sum(stats_dict['Protection'])
    evasion = sum_stat('Evasion', stats_dict, player_stats)
    regen = sum_stat('Regeneration', stats_dict, player_stats)
    health = sum_stat_w_per('Health', 'Health Percent', stats_dict, player_stats)

    melee_reduced = damage * reduced_damage(evasion_reduction(evasion)) * (resistance / 100)
    melee_damage = hits * (melee_reduced * reduced_damage(armor_reduction(armor, toughness, melee_reduced)) * reduced_damage(protection_reduction(protection)))
    damage_percent = (melee_damage - regeneration(regen, melee_damage)) / health

    return damage_percent