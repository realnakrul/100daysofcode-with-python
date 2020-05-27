import os
from urllib.request import urlretrieve
import csv

BASE_URL = 'https://raw.githubusercontent.com/mikeckennedy/data-1/master/thanksgiving-2015/'
BASE_FOLDER = os.path.dirname(__file__)
SUB_FOLDER = 'Data'
RAW_DATA = 'thanksgiving-2015-poll-data.csv'
DATA = []


def init():
    local_data = os.path.join(BASE_FOLDER, SUB_FOLDER, RAW_DATA)
    if not os.path.exists(local_data):
        remote_data = os.path.join(BASE_URL, RAW_DATA)
        urlretrieve(remote_data, local_data)
        #TODO: Doesn't work in Windows, something wrong with path
    return local_data


def read_csv(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            DATA.append(row)


def init_qestionare(data):
    regions = set()
    income = set()
    for line in data:
        if line['US Region']:
            regions.add(line['US Region'])
        if line['How much total combined money did all members of your HOUSEHOLD earn last year?']:
            income.add(line['How much total combined money did all members of your HOUSEHOLD earn last year?'])
    return regions, income


def select_option(options_list, question):
    options_dict = {index: line for index, line in enumerate(options_list, 1)}
    for index in options_dict:
        print(f'{index} {options_dict[index]}')
    # TODO: Check result for correct input
    print(f'Select your {question} (1-{len(options_list)}):')
    result = int(input())
    return options_dict[result]


def get_dishes(data, region, income):
    result = set()
    for line in data:
        if line['US Region'] == region and line['How much total combined money ' 
                'did all members of your HOUSEHOLD earn last year?'] == income and line['What is typically ' 
                'the main dish at your Thanksgiving dinner?']:
            result.add(line['What is typically the main dish at your Thanksgiving dinner?'])
    print(result)


if __name__ == '__main__':
    raw_csv_file = init()
    read_csv(raw_csv_file)
    regions_list, income_list = init_qestionare(DATA)
    region = select_option(regions_list, 'region')
    income = select_option(income_list, 'income range')
    print('Possible options are:')
    get_dishes(DATA, region, income)
