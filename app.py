from flask import Flask, jsonify, g 

from flask_cors import CORS

from resources.movies import movie 

import models 

DEBUG = True  # this give me errors 
PORT = 8000 # Port the flask app is going to run on


# initializing the flask object and making an app out of it 
app = Flask(__name__)
CORS(app)


# @app.route("/")
# def index():
#   return "hi eder"


# @app.route("/json")
# def movie():
#   return jsonify(title="boo", genre="horror")

# @app.route("/sayhi/<username>")
# def hello(username):
#   return "Hello {}".format(username)


@app.before_request #decorator function that runs before function
def before_request():
# this connect to a db before a request
  g.db = models.DATABASE
  g.db.connect()

# CORS connection here to REACT App, this is the url from heroku that will use our api 
CORS(movie, origins=['https://localhost:3000'], 
# allows cookies to be sent to our api
supports_credentials=True)



# Register blueprint here to models 
app.register_blueprint(movie, url_prefix='/api/v1/movies')


@app.after_request
def after_request(response):
# this close db connection after each request
  g.db.close()
  return response #respone will be some json 




# this runs the app run hwne the program starts
if __name__ == '__main__':
  models.initialize() #invokes function to create tables in models.py
  app.run(debug=DEBUG, port=PORT) 