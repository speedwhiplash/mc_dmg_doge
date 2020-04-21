import argparse

from compare import compare

# Code description
parser = argparse.ArgumentParser(description='Find the best armor build given a situation.')

# Add command-line arguments
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
                    help='filters consumables, True means must contain, False means must not contain, None is default')

# Compile the arguments
compare(parser.parse_args())
