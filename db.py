from tmdbv3api import TMDb, Movie
import redis


class db:
    api_key = ""
    redis_server = None
    
    def __init__(self, api_key):
        self.api_key = api_key


    def start(self):
        movie = Movie()
        self.redis_server = redis.StrictRedis(host='docker_redis', port=6379, db=0)
        tmdb = TMDb()
        tmdb.api_key = self.api_key
        self.getPopular(movie)

    def getPopular(self, movie):
        popular = movie.popular()
        self.saveMovies(popular)


    def saveMovies(self, eachMovie):
        with self.redis_server.pipeline() as pipe:
            for eachMovie in eachMovie:
                pipe.hset(eachMovie.title, "title" ,eachMovie.title)
                pipe.hset(eachMovie.title, "overview" ,eachMovie.overview)
                pipe.hset(eachMovie.title, "poster_path" ,eachMovie.poster_path)
                pipe.hset(eachMovie.title, "vote_count", eachMovie.vote_count)
                pipe.hset(eachMovie.title, "id", eachMovie.id)
            pipe.execute()    