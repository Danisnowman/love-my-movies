from tmdbv3api import TMDb, Movie
import redis, random, json



class db:
    api_key = ""
    r = None
    
    def __init__(self, api_key):
        self.api_key = api_key


    def start(self):
        movie = Movie()
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        tmdb = TMDb()
        tmdb.api_key = self.api_key
        self.getPopular(movie)

    def getPopular(self, movie):
        popular = movie.popular()
        self.saveMovies(popular)

    # def addMoviesToList(self, movies):
    #     movie_list = []
    #     for eachMovie in movies:
    #         self.saveMovies(eachMovie)
    #         # cleared_movie = {
    #         #         f"{eachMovie.title}" : {
    #         #         "poster_path" : f"{eachMovie.poster_path}",
    #         #         "overview" : f"{eachMovie.overview}",
    #         #         "vote_count" : f"{eachMovie.vote_count}",
    #         #         "imdb_id" : f"{eachMovie.imdb_id}"
    #         #     }
    #         # }
    #         # cleared_movie = customMovie(eachMovie.poster_path,eachMovie.title, eachMovie.id, eachMovie.overview, eachMovie.vote_count)
    #         movie_list.append(cleared_movie)
    #     self.saveMovies(movie_list)

    def saveMovies(self, eachMovie):
        # print(eachMovie)
        with self.r.pipeline() as pipe:
            # json_movies = json.dumps(eachMovie)
            for eachMovie in eachMovie:
                pipe.hset(eachMovie.title, "poster_path" ,eachMovie.poster_path)
                pipe.hset(eachMovie.title, "vote_count", eachMovie.vote_count)
                pipe.hset(eachMovie.title, "id", eachMovie.id)

            pipe.execute()    