from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///movies.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    genre = Column(String)
    
romance_movies=session.query(Movie).filter_by(genre=='Romance')
all_movies=session.query(Movie).order_by(Movie.movie_title.asc())