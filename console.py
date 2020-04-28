import argparse

from compare import compare

# Code description
parser = argparse.ArgumentParser(description='Find the best armor build given a situation.')

# Add command-line arguments
parser.add_argument('damage', metavar='damage', default=30.0, type=float, nargs='?',
                    help='received damage from an attack, highest in the Celsian Isles is 30.0')

parser.add_argument('hits_taken', metavar='hits taken', default=0.0, type=float, nargs='?',
                    help='number of hits taken in 3 seconds')

parser.add_argument('damage_absorbed', metavar='damage absorbed', default=100.0, type=float, nargs='?',
                    help='base damage absorbed from an attack, usually 100.0.')

parser.add_argument('armor', metavar='armor', default=0.0, type=float, nargs='?',
                    help='base armor your character has, usually 0.0')

parser.add_argument('armor_percent', metavar='armor percent', default=100.0, type=float, nargs='?',
                    help='base percent armor your character has, usually 100.0.')

parser.add_argument('toughness', metavar='toughness', default=0.0, type=float, nargs='?',
                    help='base toughness your character has, usually 0.0')

parser.add_argument('toughness_percent', metavar='toughness percent', default=100.0, type=float, nargs='?',
                    help='base percent toughness your character has, usually 100.0.')

parser.add_argument('evasion', metavar='evasion', default=0.0, type=float, nargs='?',
                    help='base points of evasion your character has, usually 0.0')

parser.add_argument('regen', metavar='regen', default=0.0, type=float, nargs='?',
                    help='base points of regen your character has, usually 0.0')

parser.add_argument('health', metavar='health', default=20.0, type=float, nargs='?',
                    help='base health your character has, usually 20.0')

parser.add_argument('health_percent', metavar='health percent', default=100.0, type=float, nargs='?',
                    help='base percent health your character has, usually 100.0.')

# Compile the arguments
compare(parser.parse_args())
