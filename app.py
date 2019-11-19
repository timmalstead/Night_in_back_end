from flask import Flask 

DEBUG = True  # this give me errors 
PORT = 8000 # Port the flask app is going to run on


# initializing the flask object and making an app out of it 
app = Flask(__name__)


@app.route('/')
def index():
  return 'hi eder'

# this runs the app run hwne the program starts
if __name__ == '__main__':
  app.run(debug=DEBUG, port=PORT)