#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Movie

fake = Faker()

def make_movies():
    """Generate and add random movies to the database."""
    Movie.query.delete()  # Clear existing movies
    
    movies = []
    generated_titles = set()  # Set to track generated titles
    
    for _ in range(50):
        while True:
            title = fake.sentence(nb_words=4).title()
            if title not in generated_titles:
                generated_titles.add(title)
                break
        
        movie = Movie(title=title)
        movies.append(movie)

    try:
        db.session.add_all(movies)
        db.session.commit()
        print("Movies successfully added to the database.")
    except Exception as e:
        db.session.rollback()
        print(f"Error adding movies: {e}")

if __name__ == '__main__':
    with app.app_context():
        make_movies()
