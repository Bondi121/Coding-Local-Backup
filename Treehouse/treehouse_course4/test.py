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
    movie_title = Column(String())
    genre = Column(String())

    def __repr__(self):
        return f'<User(movie_title={self.movie_title}, genre={self.genre})>'


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    new_movie = Movie(movie_title = "Lord of the rings", genre = "Fantasy")
    session.add(new_movie)
    session.commit()