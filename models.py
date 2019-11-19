# import * = import everything from peeweee.   Flask to db
from peewee import * 
#peeweee is like  mongoose, allows me to talk to my database



DATABASE = SqliteDatabase('movies.sqlite')
#sqllite db are easy to change to we use them 

# creating a movie class and inheriting from the model class 
class Movie(Model):
  title = CharField() # for strings  
  genre = CharField()

  class Meta:  # tells model to connect to specific db
    database = DATABASE


def initialize(): #making the name up , defining  a method, so not calling rn 
  
  DATABASE.connect()
  DATABASE.create_tables([Movie], safe=True) #if table was created do no delete it 

  print("TABLES Created")
  DATABASE.close()