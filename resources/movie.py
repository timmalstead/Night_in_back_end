import models 
from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict

movie = Blueprint('movie','movie')

@movie.route('/',methods=["GET"])
def fetch_movies():
        movies = [model_to_dict(movie) for movie in models.movie.select()]
        return jsonify(data=movies, status={"code": 200, "message": "Success"})