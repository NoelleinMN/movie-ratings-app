"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime, date

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()


# Load movie data from JSON file
with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # overview, poster_path, release_date, title = movies_in_db.append(movie)

    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. 
    
    # could possibly do list unpacking since movies.json is a list of dictionaries
    # overview, poster_path, release_date, title = movies_in_db.append()
    overview = movie['overview']
    poster_path = movie['poster_path']
    title = movie['title']
   
    #Then, get the release_date and convert it to a datetime object with datetime.strptime
    date_str = movie['release_date']
    format = "%Y-%m-%d"
    release_date = datetime.strptime(date_str, format)
    
    add_movie_db = crud.create_movie(title, overview, release_date, poster_path)
    
    # TODO: create a movie here and append it to movies_in_db
    movies_in_db.append(add_movie_db)
    # return movies_in_db

# adding fake users to the database

for n in range(10):
    email = f'fakeuser{n}@fakeuser.com' # the n will make each user different
    password = 'password'           # password does not have to be unique

    # TODO: create a user here
    user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    for mov_score in range(10):
        rand_mov = choice(movies_in_db)
        score = randint(1,5)
        crud.create_rating(user, rand_mov, score)

