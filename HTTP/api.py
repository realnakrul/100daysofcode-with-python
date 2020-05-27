import requests
from collections import namedtuple
from typing import List


Episode = namedtuple('Episode', 'category, id, url, title, description')


def search_episodes(keyword):
    url = f'https://search.talkpython.fm/api/search?q={keyword}'
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()
    episodes = []
    for r in results['results']:
        if r['category'] == 'Episode':
            episodes.append(r)
    return episodes


def search_episodes_ng(keyword: str) -> List[Episode]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()
    episodes = []
    for r in results['results']:
        if r['category'] == 'Episode':
            episodes.append(Episode(**r))
    return episodes
