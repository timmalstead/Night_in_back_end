import models 

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict 


movie = Blueprint("movies", "movie")
# V 

@movie.route('/', methods=["GET"])
def get_all_movies():
    try: # model to dict = 
      movies = [model_to_dict(movie) for movie in models.Movie.select()]
      print(movies, "THIS IS MOVIES")
      return jsonify(data=movies, status={"code":200, "messages" : "Success"})
    except models.DoesNotExist:
      return jsonify(data={}, status={"code":401, "message": "Error "})

