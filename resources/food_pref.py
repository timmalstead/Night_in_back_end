import models 
from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict
food_pref = Blueprint('food_pref', 'food_pref')

@food_pref.route('/register',methods=["POST"])
def register():
    payload = request.get_json()
    pref = models.food_pref.create(**payload)
    print(pref)
    pref_dict = model_to_dict(pref)
    return jsonify(data=pref_dict, status={"code":201,"message":"Success"})

@food_pref.route('/<user_id>',methods=["GET"])
def fetch_by_user(user_id):
    print(user_id) 
    user = models.User.get_by_id(user_id)

    
    pref = models.food_pref.select().get()
    user_model = user.food_prefs.get()
    # print(type(pref))
    # print(type(user_model))
    # print(user_model)


    
    
    return jsonify(data=model_to_dict(user_model), status={"code":201,"message":"Success"})

@food_pref.route('/<user_id>',methods=["PUT"])
def update_food_prefs(user_id):
    payload = request.get_json()
    user = models.User.get_by_id(user_id)
    user_model = user.food_prefs.get()
    query = user_model.update(**payload)
    query.execute()
    user1 = models.User.get_by_id(user_id)
    user_model1 = user.food_prefs.get()

    return jsonify(data=model_to_dict(user_model1), status={"code":201,"message":"Success"})
