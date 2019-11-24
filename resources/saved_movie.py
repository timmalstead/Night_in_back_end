import models 
from flask import request, jsonify, Blueprint 
from playhouse.shortcuts import model_to_dict
saved_movie = Blueprint('saved_movie', 'saved_movie')

@saved_movie.route('/',methods=["POST"])
def create_favorite():
    payload = request.get_json()
    favorite = models.saved_movie.create(**payload)
    favorite_dict = model_to_dict(favorite)
    return jsonify(data=favorite_dict, status = {"code": 201, "message": "Success"})

@saved_movie.route('/<id>',methods=["GET"]) #id of user
def get_users_favorite(id):
    try:
        user = models.User.get_by_id(id)
        favorites = [model_to_dict(movie) for movie in user.saved_movies.select()]
        return jsonify(data=favorites, status={"code": 200, "message": "resource deleted successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@saved_movie.route('/<id>',methods=["DELETE"]) #id of saved_movie
def delete_favorite(id):
    query = models.saved_movie.delete().where(models.saved_movie.id == id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})