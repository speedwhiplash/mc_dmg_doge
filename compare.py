import data
import logic

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

#Compile the arguments
args = parser.parse_args()