import models 
from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict

saved_food = Blueprint('saved_food', 'saved_food')

@saved_food.route('/',methods=["POST"])
def create_favorite():
    payload = request.get_json()
    favorite = models.saved_food.create(**payload)
    favorite_dict = model_to_dict(favorite)
    del favorite_dict['user']
    return jsonify(data=favorite_dict, status = {"code": 201, "message": "Success"})

@saved_food.route('/<id>',methods=["GET"])
def get_users_favorite(id):
    try:
        user = models.User.get_by_id(id)
        favorites = [model_to_dict(food) for food in user.saved_foods.select()]
        for favorite in favorites:
            del favorite['user']
        return jsonify(data=favorites, status={"code": 200, "message": "resource retrieved successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@saved_food.route('/<id>',methods=["DELETE"])
def delete_favorite(id):
    query = models.saved_food.delete().where(models.saved_food.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})