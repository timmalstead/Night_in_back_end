UNDER CONSTRUCTION 

import models 

from flask import request, jsonify, Blueprint 

from playhouse.shortcuts import model_to_dict

movie_pref = Blueprint('movie_prefs', 'movie_pref')

@movie_pref.route('/',methods=["POST"])
def register():
    payload = request.get_json()

    try:
        models.movie_pref.get(models.movie_pref.user === payload ['user_id'])
        return jsonify(data={}, status={"code":401, "message":"A user with that email already exists"})
    except models.DoesNotExist:
        movie_pref = models.movie_pref.create(**payload)

        movie_pref_dict = model_to_dict(list)
        return jsonify(data = list_dict, status={"code": 201, "message": "Success"})
        
@movie_pref.route('/',methods=["GET"])
def get_movie_pref():
    try:
        movie_prefs = [model_to_dict(movie_pref) for movie_pref in modles.movie_pref.select().where(movie_pref.user == )