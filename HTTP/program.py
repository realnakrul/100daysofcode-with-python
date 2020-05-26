import api


def main():
    print('* talkpython.fm episodes search program *')
    episodes = api.search_episodes(input('Enter your keyword: '))
    print(f'Found: {len(episodes)}')
    for index, e in enumerate(episodes, 1):
        print(f'{index}. {e["title"]}')


if __name__ == '__main__':
    main()
