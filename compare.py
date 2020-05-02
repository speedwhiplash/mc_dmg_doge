import time

from armor_data import read_armor_data
from logic import *
from player_data import player_data


def compare(args):
    print(f"started at {time.strftime('%X')}")

    all_armor_stats = read_armor_data()
    player_stats = player_data(args)

    stats_to_track = ['Armor', 'Armor Percent', 'Toughness', 'Toughness Percent', 'Protection', 'Health', 'Health Percent', 'Evasion', 'Regeneration']

    slot_idxs, values = create_slot_counters(all_armor_stats)

    deep_compare(all_armor_stats, slot_idxs, values, 0, stats_to_track, player_stats, args.damage, args.hits_taken)
    print(f"finished at {time.strftime('%X')}")

    best_idxs = get_best()

    print(best_idxs)
    print(
        all_armor_stats[0][best_idxs[0]]['Name'] + ', ',
        all_armor_stats[1][best_idxs[1]]['Name'] + ', ',
        all_armor_stats[2][best_idxs[2]]['Name'] + ', ',
        all_armor_stats[3][best_idxs[3]]['Name'] + ', ',
        all_armor_stats[4][best_idxs[4] - 1]['Name']
    )
