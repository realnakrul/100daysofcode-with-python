from api import MovieSearchClient


def search_by_keyword():
    svc = MovieSearchClient()
    keyword = input('Enter keyword to search: ')
    response = svc.search(keyword)
    print(response)
    if response.json():
        for hit in response.json()['hits']:
            print(hit['title'])


if __name__ == '__main__':
    search_by_keyword()
