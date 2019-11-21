import datetime 
from peewee import * 
from flask_login import UserMixin 



DATABASE = SqliteDatabase('night_in.sqlite',pragmas={'foreign_keys': 1})



#BaseModel allows us not to have put class meta on every table
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

class movie(Model):
  url = CharField()
  genre = CharField()
  image = CharField()
  title = CharField()
  year = IntegerField()
  class Meta:
    database = DATABASE

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

class movie_pref(BaseModel):
  user = ForeignKeyField(User, backref='movie_prefs')
  horror = BooleanField(default = False)
  comedy = BooleanField(default = False)
  romance = BooleanField(default = False)
  animation = BooleanField(default = False)
  drama = BooleanField(default = False)
  sci_fi = BooleanField(default = False)
  crime = BooleanField(default = False)
  mystery = BooleanField(default = False)
  adventure = BooleanField(default = False)
  thriller = BooleanField(default = False)
  fantasy = BooleanField(default = False)
  musical = BooleanField(default = False)
  silent = BooleanField(default = False)
  western = BooleanField(default = False)
  war = BooleanField(default = False)
  action = BooleanField(default = False)
  biography = BooleanField(default = False)

class night(BaseModel):
  user = ForeignKeyField(User, backref='food_prefs')
  movie_id = CharField()
  meal_id=CharField()
  created_at = DateTimeField(default=datetime.datetime.now)






def initialize(): #making the name up , defining  a method, so not calling rn 
  
  DATABASE.connect()
  DATABASE.create_tables([User,saved_movie,movie,saved_food,food_pref,movie_pref,night], safe=True) #if table was created do no delete it 
  print("TABLES Created")
  DATABASE.close()