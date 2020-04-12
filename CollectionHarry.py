from collections import Counter
import os
from urllib.request import urlretrieve
from pprint import pprint
import re

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fharry = 'harry.txt'
fstop = 'stopwords.txt'
remote_harry = os.path.join(BASE_URL, fharry)
local_harry = os.path.join(TMP, fharry)
remote_stop = os.path.join(BASE_URL, fstop)
local_stop = os.path.join(TMP, fstop)
urlretrieve(remote_harry, local_harry)
urlretrieve(remote_stop, local_stop)


if __name__ == '__main__':
    '''Solution to PyBites Bite 18'''
    with open(local_harry) as f:
        harry_text = f.read()
    # print(harry_text.lower().split())
    harry_counter = Counter(re.split(r'[ ,.\n!?:;\"\-]+', harry_text.lower()))
    with open(local_stop) as f:
        stop_text = f.read()
    # print(stop_text)
    for s in stop_text.split():
        del harry_counter[s]
    print(harry_counter.most_common(1))