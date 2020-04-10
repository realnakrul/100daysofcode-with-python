from datetime import datetime
import os
import urllib.request
from pprint import pprint

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'shudown.log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()

pprint(loglines)
# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    _, dd, *_ = line.split()
    return datetime.strptime(dd, '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    f_events = []
    for l in loglines:
        if "Shutdown initiated" in l:
            f_events.append(convert_to_datetime(l))
    result = f_events[1] - f_events[0]
    return result


time_between_shutdowns(loglines)