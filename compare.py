from data import armor_stats
from logic import *

import argparse

#Code description
parser = argparse.ArgumentParser(description='Find the best armor build given a situation.')

#Add command-line arguments
parser.add_argument('damage_absorbed', metavar='damage absorbed', default=100.0, type=float, nargs='?',
                    help='base damage absorbed from an attack, usually 100.0.')
parser.add_argument('damage', metavar='damage', default=30.0, type=float, nargs='?',
                    help='received damage from an attack, highest in the Celsian Isles is 30.0')
parser.add_argument('weapon_damage', metavar='weapon damage', default=10.0, type=float, nargs='?',
                    help='base damage your held weapon deals, usually 10.0')
parser.add_argument('weapon_speed', metavar='weapon speed', default=1.6, type=float, nargs='?',
                    help='base attack speed your held weapon has, usually 1.6')
parser.add_argument('bow_damage', metavar='bow damage', default=10.0, type=float, nargs='?',
                    help='base damage your held bow deals, usually 10.0')
parser.add_argument('arrow_speed', metavar='arrow speed', default=0.7, type=float, nargs='?',
                    help='base bonus speed for your bow-fired arrows, usually 0')
parser.add_argument('health', metavar='health', default=20.0, type=float, nargs='?',
                    help='base health your character has, usually 20.0')
parser.add_argument('speed', metavar='speed', default=0.0, type=float, nargs='?',
                    help='base movement speed your character has: 0.15 if sprinting, 0.10 if not')
parser.add_argument('stat', metavar='stat', default='melee taken', nargs=1,
					help='what statistic to track, usually melee damage taken')
parser.add_argument('track', choices=['max', 'min'], metavar='track', default='min', nargs=1,
					help='whether to track maximum or minimum of your pick')
parser.add_argument('initial_best', metavar='guess', default=1000, nargs='?',
					help='filters your guess by setting a guess condition, usually 1000 if looking for minimum damage')
parser.add_argument('hits_taken', metavar='hits taken', default=0.0, type=float, nargs='?',
                    help='number of hits taken in 3 seconds')
parser.add_argument('filters.consumables', metavar='filter consumables', default=None, nargs='?',
					help='filters consumables, True means must contain, False means must not contain, None is default' )

#Compile the arguments
args = parser.parse_args()

all_armor_stats = armor_stats()

player_stats = {'Damage Absorbed' : args.damage_absorbed,
                'Armor Percent' : 100,
				'Toughness Percent' : 100,
				'Speed' : args.speed,
				'Speed Percent' : 100,
				'Health' : args.health,
				'Health Percent' : 100,
                'Attack Damage' : args.weapon_damage,
				'Attack Damage Percent' : 100,
				'Bow Damage' : args.bow_damage,
				'Bow Damage Percent' : 100,
				'Arrow Speed' : args.arrow_speed,
				'Attack Speed Percent' : 100,
				'Attack Speed' : args.weapon_speed,
				'Arrow Speed Percent' : 100}

stats_to_track = []
if args.stat[0]=='melee damage':
	stats_to_track = ['Armor', 'Armor Percent', 'Toughness', 'Toughness Percent', 'Protection', 'Health', 'Health Percent', 'Evasion', 'Regeneration']

if args.track[0]=='max':
	args.track = max
elif args.track[0]=='min':
	args.track = min

slot_idxs, values = create_slot_counters(all_armor_stats)

best_guess(args.initial_best)

deep_compare(all_armor_stats, slot_idxs, values, 0, args.stat[0], stats_to_track, player_stats, args.track, args.damage, args.hits_taken)

best_idxs = get_best()

print(best_idxs)
print(
	all_armor_stats[0][best_idxs[0]]['Helmet Name'],
	all_armor_stats[1][best_idxs[1]]['Chestplate Name'],
	all_armor_stats[2][best_idxs[2]]['Leggings Name'],
	all_armor_stats[3][best_idxs[3]]['Boots Name'],
	all_armor_stats[4][best_idxs[4]-1]['Offhand Name']
	)