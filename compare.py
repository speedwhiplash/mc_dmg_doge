import time

from armor_data import read_armor_data
from logic import *
from player_data import player_data


def compare(args):
    print(f"started at {time.strftime('%X')}")

    all_armor_stats = read_armor_data()
    player_stats = player_data(args)

    stats_to_track = []
    if args.stat[0] == 'melee damage':
        stats_to_track = ['Armor', 'Armor Percent', 'Toughness', 'Toughness Percent', 'Protection', 'Health', 'Health Percent', 'Evasion', 'Regeneration']

    if args.track[0] == 'max':
        args.track = max
    elif args.track[0] == 'min':
        args.track = min

    slot_idxs, values = create_slot_counters(all_armor_stats)

    best_guess(args.initial_best)

    deep_compare(all_armor_stats, slot_idxs, values, 0, args.stat[0], stats_to_track, player_stats, args.track, args.damage, args.hits_taken)
    print(f"finished at {time.strftime('%X')}")

    best_idxs = get_best()

    print(best_idxs)
    print(
        all_armor_stats[0][best_idxs[0]]['Helmet Name'] + ', ',
        all_armor_stats[1][best_idxs[1]]['Chestplate Name'] + ', ',
        all_armor_stats[2][best_idxs[2]]['Leggings Name'] + ', ',
        all_armor_stats[3][best_idxs[3]]['Boots Name'] + ', ',
        all_armor_stats[4][best_idxs[4] - 1]['Offhand Name']
    )
