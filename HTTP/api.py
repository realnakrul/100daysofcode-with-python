import requests


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
