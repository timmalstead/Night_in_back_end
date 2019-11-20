import datetime 
from peewee import * 
from flask_login import UserMixin 



DATABASE = SqliteDatabase('night_in.sqlite',pragmas={'foreign_keys': 1})




class BaseModel(Model):
 class Meta:
    database = DATABASE

class User(UserMixin,BaseModel):
  username = CharField(unique=True)
  email = CharField(unique=True)
  password = CharField()
  phone = CharField(10, default = 0)

class saved_movies(BaseModel):
  user = ForeignKeyField(User, backref='saved_movies')
  movie_id = CharField()

class saved_foods(BaseModel):
  user = ForeignKeyField(User, backref='saved_foods') 
  meal_id = CharField()

class food_prefs(BaseModel):
  user = ForeignKeyField(User, backref='food_prefs')
  beef = BooleanField()
  breakfast = BooleanField()
  chicken = BooleanField()
  dessert = BooleanField()
  goat = BooleanField()
  lamb = BooleanField()
  miscellaneous = BooleanField()
  pasta = BooleanField()
  pork = BooleanField()
  seafood = BooleanField()
  side = BooleanField()
  starter = BooleanField()
  vegan = BooleanField()
  vegetarian = BooleanField()

# class movie_prefs(BaseModel):
#   user = ForeignKeyField(User, backref='movie_prefs'):
# TBA

class nights(BaseModel):
  user = ForeignKeyField(User, backref='food_prefs')
  movie_id = CharField()
  meal_id=CharField()
  created_at = DateTimeField(default=datetime.datetime.now)






def initialize(): #making the name up , defining  a method, so not calling rn 
  
  DATABASE.connect()
  DATABASE.create_tables([User,saved_movies,saved_foods,food_prefs,nights], safe=True) #if table was created do no delete it 
  print("TABLES Created")
  DATABASE.close()