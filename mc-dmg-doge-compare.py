import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
helmets     = client.open('Armor Stats').get_worksheet(1)
chestplates = client.open('Armor Stats').get_worksheet(2)
leggings    = client.open('Armor Stats').get_worksheet(3)
boots       = client.open('Armor Stats').get_worksheet(4)
offhands    = client.open('Armor Stats').get_worksheet(5)

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