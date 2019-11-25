import models 

from flask import request, jsonify, Blueprint 
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, login_required, logout_user
from playhouse.shortcuts import model_to_dict

user = Blueprint('users', 'user')

@user.route('/register',methods=["POST"])
def register():
    payload = request.get_json()

    payload['email'].lower()
    try:
        models.User.get(models.User.email == payload ['email'])
        return jsonify(data={}, status={"code":401, "message":"A user with that email already exists"})
    except models.DoesNotExist:
        payload['password']= generate_password_hash(payload['password'])
        user = models.User.create(**payload)

        login_user(user)
        user_dict = model_to_dict(user)
        print(user_dict)
        print(type(user_dict))
        del user_dict['password']

        return jsonify(data=user_dict, status={"code": 201, "message": "Success"})


@user.route('/login', methods=["POST"])
def login():
    payload = request.get_json()
    print(payload, '< --- this is playload')
    try:
        user = models.User.get(models.User.email== payload['email'])
        user_dict = model_to_dict(user)
        if(check_password_hash(user_dict['password'], payload['password'])):
            del user_dict['password']
            login_user(user)
            print(user, ' this is user')
            return jsonify(data=user_dict, status={"code": 200, "message": "Success"})
        else:
            return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Username or Password is incorrect"})

@user.route('/logout',methods=["GET"])
@login_required
def logout():
    
    logout_user()
    return ('you are logged out')


#delete
@user.route('/delete',methods=["DELETE"])
@login_required
def delete():
    
    user = models.User.get_by_id(str(current_user))
    print(current_user)
    user.delete().execute()
    logout_user()
    return jsonify(data='user account successfully deleted', status={"code":200, "message": "resource deleted successfully"})
#edit

@user.route('/edit',methods=["PUT"])
@login_required
def update_user():
    payload = request.get_json()
    # payload['password']= generate_password_hash(payload['password'])
    query = models.User.update(**payload).where(models.User.id==str(current_user))
    query.execute()
    return jsonify(data=model_to_dict(models.User.get_by_id(str(current_user))), status={"code": 200, "message": "resource updated successfully"})
