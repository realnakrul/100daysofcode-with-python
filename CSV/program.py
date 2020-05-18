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
    return local_data


def read_csv(file):
    with open(file) as f:
        reader = csv.DictReader(f)
        for row in reader:
            DATA.append(row)


def get_regions(data):
    result = set()
    for line in data:
        if line['US Region']:
            result.add(line['US Region'])
    return result


def select_region(regions):
    print(f'Select region (1-{len(regions)}):')
    for index, line in enumerate(regions, 1):
        print(f'{index} {line}')
    result = input()
    # TODO: Fix selection to return region, not a number
    return result


if __name__ == '__main__':
    raw_csv_file = init()
    read_csv(raw_csv_file)
    select_region(get_regions(DATA))