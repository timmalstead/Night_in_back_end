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

class saved_movie(BaseModel):
  user = ForeignKeyField(User, backref='saved_movies')
  movie_id = CharField()

class saved_food(BaseModel):
  user = ForeignKeyField(User, backref='saved_foods') 
  meal_id = CharField()

class food_pref(BaseModel):
  user = ForeignKeyField(User, backref='food_prefs')
  beef = BooleanField(default = False)
  breakfast = BooleanField(default = False)
  chicken = BooleanField(default = False)
  dessert = BooleanField(default = False)
  goat = BooleanField(default = False)
  lamb = BooleanField(default = False)
  miscellaneous = BooleanField(default = False)
  pasta = BooleanField(default = False)
  pork = BooleanField(default = False)
  seafood = BooleanField(default = False)
  side = BooleanField(default = False)
  starter = BooleanField(default = False)
  vegan = BooleanField(default = False)
  vegetarian = BooleanField(default = False)

# class movie_prefs(BaseModel):
#   user = ForeignKeyField(User, backref='movie_prefs'):
# TBA

class night(BaseModel):
  user = ForeignKeyField(User, backref='food_prefs')
  movie_id = CharField()
  meal_id=CharField()
  created_at = DateTimeField(default=datetime.datetime.now)






def initialize(): #making the name up , defining  a method, so not calling rn 
  
  DATABASE.connect()
  DATABASE.create_tables([User,saved_movie,saved_food,food_pref,night], safe=True) #if table was created do no delete it 
  print("TABLES Created")
  DATABASE.close()