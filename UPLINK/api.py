import uplink


@uplink.json
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm/')

    @uplink.get('/api/search/{keyword}')
    def search(self, keyword):
        """ Get's all movies by keyword. """
