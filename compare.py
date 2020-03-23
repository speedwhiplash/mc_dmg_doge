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

#Compile the arguments
args = parser.parse_args()
damage = args.damage
weapon_damage = args.weapon_damage
weapon_speed = args.weapon_speed
bow_damage = args.bow_damage
arrow_speed = args.arrow_speed
health = args.health
speed = args.speed
pick = args.pick[0]
track = args.track[0]

armor_stats = armor_stats()
player_stats = player_stats()[0]

for key,value in player_stats.items():
	if key=='Speed':
		player_stats['Speed'] = speed
	if key=='Health':
		player_stats['Health'] = health
	if key=='Attack Damage':
		player_stats['Attack Damage'] = weapon_damage
	if key=='Bow Damage':
		player_stats['Bow Damage'] = bow_damage
	if key=='Arrow Speed':
		player_stats['Arrow Speed'] = arrow_speed
	if key=='Attack Speed':
		player_stats['Attack Speed'] = weapon_speed

armor_combinations = list(product(*(armor_stats[key] for key in armor_stats)))

for i in range(len(armor_combinations)):
	armor_combinations[i] = list(armor_combinations[i])
	armor_combinations[i].append(player_stats)

for i in range(len(armor_combinations)):
	current_combo = armor_combinations[i]
	current_combo = repeated_merge(current_combo)
	current_combo['Armor'] *= current_combo['Armor Percent']/100.0
	del(current_combo['Armor Percent'])
	current_combo['Toughness'] *= current_combo['Toughness Percent']/100.0
	del(current_combo['Toughness Percent'])
	current_combo['Speed Percent'] = total(current_combo['Speed'],current_combo['Speed Percent']/100.0)/player_stats['Speed']
	del(current_combo['Speed'])
	current_combo['Health'] *= current_combo['Health Percent']/100.0
	del(current_combo['Health Percent'])
	current_combo['Attack Damage'] *= current_combo['Attack Damage Percent']/100.0
	del(current_combo['Attack Damage Percent'])
	current_combo['Bow Damage'] *= current_combo['Bow Damage Percent']/100.0
	del(current_combo['Bow Damage Percent'])
	current_combo['Attack Speed'] *= current_combo['Attack Speed Percent']/100.0
	del(current_combo['Attack Speed Percent'])
	current_combo['Arrow Speed Percent'] = total(current_combo['Arrow Speed'],current_combo['Arrow Speed Percent']/100.0)/current_combo['Arrow Speed']
	del(current_combo['Arrow Speed'])
	armor_combinations[i] = current_combo