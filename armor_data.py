import ast
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def _get_from_spreadsheet():
    # Removes all instances of '' from a list of
    # dictionaries and replaces them with 0.
    def fix_zeros(dict_list):
        for dict in range(len(dict_list)):
            for key, value in dict_list[dict].items():
                if value == '':
                    dict_list[dict][key] = 0
        return dict_list

    # Log into the service account with credentials given by a private key.
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('mc-dmg-doge-reader.json', scope)
    client = gspread.authorize(creds)

    # Open every worksheet.
    stats = client.open('Armor Stats')
    helmet_stats = stats.get_worksheet(0)
    chestplate_stats = stats.get_worksheet(1)
    legging_stats = stats.get_worksheet(2)
    boot_stats = stats.get_worksheet(3)
    offhand_stats = stats.get_worksheet(4)

    # Get the key-value pairs of data from every worksheet.
    helmet_data = helmet_stats.get_all_records()
    chestplate_data = chestplate_stats.get_all_records()
    legging_data = legging_stats.get_all_records()
    boot_data = boot_stats.get_all_records()
    offhand_data = offhand_stats.get_all_records()

    # set clean data.
    armor_data = [
        fix_zeros(helmet_data),
        fix_zeros(chestplate_data),
        fix_zeros(legging_data),
        fix_zeros(boot_data),
        fix_zeros(offhand_data)
    ]

    with open('armor_stats.json', 'w') as stats_file:
        json.dump(armor_data, stats_file)
    try:
        stats_file.close()
    except Exception as err:
        raise ValueError('Could not close file. {0}'.format(err))
        pass

    return armor_data


# First try local file, or build from workbooks
def read_armor_data():
    try:
        with open('armor_stats.json') as file:
            armor_data = json.load(file)
            armor_data = ast.literal_eval(armor_data)
            file.close()
    except:
        armor_data = _get_from_spreadsheet()

    if armor_data == [] or armor_data == {} or armor_data is None:
        return _get_from_spreadsheet()

    return [
        armor_data[0],
        armor_data[1],
        armor_data[2],
        armor_data[3],
        armor_data[4]
    ]
