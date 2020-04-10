import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
from pprint import pprint
from operator import itemgetter

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    m_by_d = defaultdict(list)
    with open(MOVIE_DATA) as f:
        movie_meta = csv.DictReader(f)
        #print(movie)
        for m in movie_meta:
            #print(m)
            try:
                title = m['movie_title'].strip()
                year = int(m['title_year'])
                score = float(m['imdb_score'])
                director = m['director_name']
            except Exception as e:
                continue
            if year > MIN_YEAR:
                decoded_m = Movie(title=title, year=year, score=score)
                m_by_d[director].append(decoded_m)
    return m_by_d


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    f_avg = 0.0
    for mo in movies:
        f_avg = f_avg + mo.score
    f_avg = round(f_avg / len(movies), 1)
    return f_avg


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    avg_by_d = []
    for d in directors:
        avg = 0.0
        if len(directors[d]) >= MIN_MOVIES:
            avg_by_d.append((d, calc_mean_score(directors[d])))
    avg_by_d = sorted(avg_by_d, key=itemgetter(1), reverse=True)
    return avg_by_d

if __name__ == '__main__':
    pprint(get_average_scores(get_movies_by_director()))