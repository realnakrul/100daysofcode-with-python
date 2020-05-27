import api
import webbrowser


def main():
    print('* talkpython.fm episodes search program *')
    episodes = api.search_episodes(input('Enter your keyword: '))
    print(f'Found: {len(episodes)}')
    for index, e in enumerate(episodes, 1):
        print(f'{index}. {e["title"]}')


def main_ng():
    print('* next generation talkpython.fm episodes search program *')
    episodes = api.search_episodes_ng(input('Enter your keyword: '))
    print(f'Found: {len(episodes)}')
    for e in episodes:
        print(f'{e.id}. {e.title}')
    # TODO: Sort list by ID
    open_episode(episodes)


def open_episode(episodes):
    try:
        open_id = int(input('Open episode #: '))
    except ValueError:
        print('Should be number')

    for e in episodes:
        if open_id == e.id:
            print(f'Opening: talkpython.fm{e.url}')
            webbrowser.open(f'talkpython.fm{e.url}', new=2)


if __name__ == '__main__':
    main_ng()
