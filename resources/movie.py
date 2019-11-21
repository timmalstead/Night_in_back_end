import models 

from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict

movie = Blueprint('movie','movie')

#By single genre 
@movie.route('/',methods=["GET"])
def fetch_by_genre():
    
        
        movies = [model_to_dict(movie) for movie in models.movie.select()]
        thing = jsonify(movies)
        print(thing)

        
        return jsonify(data=movies, status={"code": 200, "message": "Success"})

        

