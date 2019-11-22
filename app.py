from flask import Flask, jsonify, g 
from flask_cors import CORS
from flask_login import LoginManager

DEBUG = True  # this give me errors 
PORT = 8000 # Port the flask app is going to run on

import models 

from resources.user import user
from resources.movie import movie
from resources.movie_pref import movie_pref
from resources.food_pref import food_pref

login_manager = LoginManager()

app = Flask(__name__)
CORS(app)

app.secret_key = "LJAKLJLKJJLJKLSDJLKJASD" ## Need this to encode the session
login_manager.init_app(app) # set up the sessions on the app

@login_manager.user_loader # decorator function, that will load the user object whenever we access the session, we can get the user
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None 


@app.before_request #decorator function that runs before function
def before_request():
# this connect to a db before a request
  g.db = models.DATABASE
  g.db.connect()

@app.after_request
def after_request(response):
  g.db.close()
  return response 


CORS(user, origins=['http://localhost:3000'],supports_credentials=True)
app.register_blueprint(user, url_prefix='/user')

CORS(movie, origins=['http://localhost:3000'],supports_credentials=True)
app.register_blueprint(movie, url_prefix='/movie')

CORS(movie_pref, origins=['http://localhost:3000'],supports_credentials=True)
app.register_blueprint(movie_pref, url_prefix='/movie_pref')

CORS(food_pref, origins=['http://localhost:3000'],supports_credentials=True)
app.register_blueprint(food_pref, url_prefix='/food_pref')



if __name__ == '__main__':
  models.initialize() #invokes function to create tables in models.py
  app.run(debug=DEBUG, port=PORT) 