from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Movie(db.Model, SerializerMixin):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer)
    genre = db.Column(db.String(100))
    director = db.Column(db.String(100))
    plot = db.Column(db.Text)

    def __repr__(self):
        return f'<Movie {self.title} ({self.release_year})>'

    def to_dict(self):
        """Converts the Movie object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'release_year': self.release_year,
            'genre': self.genre,
            'director': self.director,
            'plot': self.plot
        }

# Example of defining a relationship (if needed):
# class Actor(db.Model):
#     __tablename__ = 'actors'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     movies = db.relationship('Movie', secondary='movie_actors', backref='actors')

# Example of validation (if needed):
# from sqlalchemy.orm import validates
# @validates('release_year')
# def validate_release_year(self, key, release_year):
#     if release_year < 1900 or release_year > 2100:
#         raise ValueError('Release year must be between 1900 and 2100.')
#     return release_year
