import gspread
from oauth2client.service_account import ServiceAccountCredentials

import argparse

#Code description
parser = argparse.ArgumentParser(description='Find the best armor build given a situation.')

#Add command-line arguments
parser.add_argument('damage', metavar='damage', default=30.0, type=float, nargs='?',
                    help='received damage from an attack')
parser.add_argument('weapon_damage', metavar='weapon damage', default=10.0, type=float, nargs='?',
                    help='base damage your held weapon deals')
parser.add_argument('weapon_speed', metavar='weapon speed', default=1.6, type=float, nargs='?',
                    help='base attack speed your held weapon has')
parser.add_argument('bow_damage', metavar='bow damage', default=10.0, type=float, nargs='?',
                    help='base damage your held bow deals')
parser.add_argument('arrow_speed', metavar='arrow speed', default=0.0, type=float, nargs='?',
                    help='base bonus speed for your bow-fired arrows')

#Compile the arguments
args = parser.parse_args()

#Removes all instances of '' from a list of
#dictionaries and replaces them with 0.
def fix_zeros(dict_list):
	for dict in range(len(dict_list)):
		for key, value in dict_list[dict].items():
			if value == '':
				dict_list[dict][key] = 0
	return(dict_list)

#Log into the service account with credentials given by a private key.
scope  = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds  = ServiceAccountCredentials.from_json_keyfile_name('mc-dmg-doge-reader.json', scope)
client = gspread.authorize(creds)

#Open every worksheet.
stats       = client.open('Armor Stats')
helmets     = stats.get_worksheet(0)
chestplates = stats.get_worksheet(1)
leggings    = stats.get_worksheet(2)
boots       = stats.get_worksheet(3)
offhands    = stats.get_worksheet(4)

#Get the key-value pairs of data from every worksheet.
helmet_data     = helmets.get_all_records()
chestplate_data = chestplates.get_all_records()
legging_data    = leggings.get_all_records()
boot_data       = boots.get_all_records()
offhand_data    = offhands.get_all_records()

#Clean up the data.
helmet_data     = fix_zeros(helmet_data)
chestplate_data = fix_zeros(chestplate_data)
legging_data    = fix_zeros(legging_data)
boot_data       = fix_zeros(boot_data)
offhand_data    = fix_zeros(offhand_data)