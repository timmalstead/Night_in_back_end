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
    print(user_id) 
    user = models.User.get_by_id(user_id)
    pref = models.movie_pref.select().get()
    user_model = user.movie_prefs.get()    
    return jsonify(data=model_to_dict(user_model), status={"code":201,"message":"Success"})

@movie_pref.route('/<user_id>',methods=["PUT"])
def update_movie_prefs(user_id):
    payload = request.get_json()
    user = models.User.get_by_id(user_id)
    user_model = user.movie_prefs.get()
    query = user_model.update(**payload)
    query.execute()
    updated_user = models.User.get_by_id(user_id)
    updated_user_model = user.movie_prefs.get()

    return jsonify(data=model_to_dict(updated_user_model1), status={"code":201,"message":"Success"})
