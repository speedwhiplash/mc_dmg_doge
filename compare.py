from data import armor_stats, player_stats
from logic import *
from itertools import product

import argparse

#Code description
parser = argparse.ArgumentParser(description='Find the best armor build given a situation.')

#Add command-line arguments
parser.add_argument('damage', metavar='damage', default=30.0, type=float, nargs='?',
                    help='received damage from an attack, highest in the Celsian Isles is 30.0')
parser.add_argument('weapon_damage', metavar='weapon damage', default=10.0, type=float, nargs='?',
                    help='base damage your held weapon deals, usually 10.0')
parser.add_argument('weapon_speed', metavar='weapon speed', default=1.6, type=float, nargs='?',
                    help='base attack speed your held weapon has, usually 1.6')
parser.add_argument('bow_damage', metavar='bow damage', default=10.0, type=float, nargs='?',
                    help='base damage your held bow deals, usually 10.0')
parser.add_argument('arrow_speed', metavar='arrow speed', default=0.0, type=float, nargs='?',
                    help='base bonus speed for your bow-fired arrows, usually 0')
parser.add_argument('health', metavar='health', default=20.0, type=float, nargs='?',
                    help='base health your character has, usually 20.0')
parser.add_argument('speed', metavar='speed', default=0.0, type=float, nargs='?',
                    help='base movement speed your character has: 0.15 if sprinting, 0.10 if not')
parser.add_argument('pick', metavar='pick', default='melee damage', nargs=1,
					help='what statistic to track, usually melee damage taken')
parser.add_argument('track', choices=['max','min'], metavar='track', default='min', nargs=1,
					help='whether to track maximum or minimum of your pick')
parser.add_argument('initial_best', metavar='guess', default=1000, nargs='?',
					help='filters your guess by setting a guess condition, usually 1000 if looking for minimum damage')

#Compile the arguments
args = parser.parse_args()

armor_stats = armor_stats()
player_stats = player_stats()[0]

player_stats['Speed'] = args.speed
player_stats['Health'] = args.health
player_stats['Attack Damage'] = args.weapon_damage
player_stats['Bow Damage'] = args.bow_damage
player_stats['Arrow Speed'] = args.arrow_speed
player_stats['Attack Speed'] = args.weapon_speed

armor_combinations = list(product(*(armor_stats[key] for key in armor_stats)))

for i in range(len(armor_combinations)):
	armor_combinations[i] = list(armor_combinations[i])
	armor_combinations[i].append(player_stats)

best = args.initial_best
best_idx = 0
for i in range(len(armor_combinations)):
	current_combo = armor_combinations[i]
	current_combo = repeated_merge(current_combo)[0]
	if args.pick[0]=='melee damage':
		armor = current_combo['Armor']*current_combo['Armor Percent']/100.0
		toughness = current_combo['Toughness']*current_combo['Toughness Percent']/100.0
		health = current_combo['Health']*current_combo['Health Percent']/100.0
	if args.pick[0]=='melee damage' and args.track[0]=='min':
		evasion_reduced_melee_damage = args.damage*reduced_damage(evasion_reduction(current_combo['Evasion']))
		melee_damage = (evasion_reduced_melee_damage*reduced_damage(armor_reduction(armor, toughness, evasion_reduced_melee_damage))*reduced_damage(protection_reduction(current_combo['Protection'])) + second_wind(current_combo['Second Wind']))/health
		if best > melee_damage:
			best = melee_damage
			best_idx = i

print(armor_combinations[best_idx])