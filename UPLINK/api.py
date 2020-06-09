import uplink


@uplink.json
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')

    @uplink.get('/api/search/{keyword}')
    def search_by_keyword(self, keyword):
        """ Get's all movies by keyword. """

    @uplink.get('/api/director/{director_name}')
    def search_by_director(self, director_name):
        """ Get's all movies by director name. """

    @uplink.get('/api/movie/top')
    def top(self):
        """ Get's top 5 movies """