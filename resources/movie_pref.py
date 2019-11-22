import models 
from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict
movie_pref = Blueprint('movie_pref', 'movie_pref')

@movie_pref.route('/register',methods=["POST"])
def register():
    payload = request.get_json()
    pref = models.movie_pref.create(**payload)
    print(pref)
    pref_dict = model_to_dict(pref)
    return jsonify(data=pref_dict, status={"code":201,"message":"Success"})

@movie_pref.route('/<user_id>',methods=["GET"])
def fetch_by_user(user_id):
    # user = models.User.get_by_id(user_id)
    pref = models.movie_pref.select()
    # .where(movie_pref.user == user_id)
    
    return jsonify(data=model_to_dict(pref), status={"code":201,"message":"Success"})

# @movie_pref.route('/',methods=["POST"])
# def register():
#     payload = request.get_json()

#     try:
#         models.movie_pref.get(models.movie_pref.user === payload ['user_id'])
#         return jsonify(data={}, status={"code":401, "message":"A user with that email already exists"})
#     except models.DoesNotExist:
#         movie_pref = models.movie_pref.create(**payload)

#         movie_pref_dict = model_to_dict(list)
#         return jsonify(data = list_dict, status={"code": 201, "message": "Success"})
        
# @movie_pref.route('/',methods=["GET"])
# def get_movie_pref():
#     try:
#         movie_prefs = [model_to_dict(movie_pref) for movie_pref in modles.movie_pref.select().where(movie_pref.user == )
