from api import MovieSearchClient


def search_by_keyword():
    svc = MovieSearchClient()
    keyword = input('Enter keyword to search: ')
    response = svc.search_by_keyword(keyword)
    # print(response)
    if response.json():
        print_results(response.json())


def search_by_director():
    svc = MovieSearchClient()
    director_name = input('Enter director name to search: ')
    response = svc.search_by_director(director_name)
    # print(response)
    if response.json():
        print_results(response.json())


def top():
    svc = MovieSearchClient()
    # director_name = input('Enter director name to search: ')
    response = svc.top()
    # print(response)
    if response.json():
        print_results(response.json())


def print_results(response):
    print(f'Found {len(response["hits"])} item(s):')
    if response['hits']:
        for index, hit in enumerate(response['hits'], 1):
            print(f'\t{index}. {hit["title"]} ({hit["year"]}) by {hit["director"]}')


if __name__ == '__main__':
    print('*** Welcome to Movie search API with UPLINK Demo ***')
    options = {
        'Top 10 Movies': top,
        'Search by keyword': search_by_keyword,
        'Search by director': search_by_director
    }
    for index, option in enumerate(options, 1):
        print(f'\t{index}. {option}')

    service = int(input(f'Select service (1-{len(options)}): '))
    option = list(options.keys())[service-1]
    print(option)
    options[option]()  # Calls function from options dictionary

    # TODO Add view item
