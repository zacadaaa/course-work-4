from unittest.mock import MagicMock
import pytest

from setup_db import db
from dao.model.director import Director
from dao.model.movie import Movie
from dao.model.genre import Genre
from dao.director import DirectorDAO
from dao.movie import MovieDAO
from dao.genre import GenreDAO


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="Director1")
    director_2 = Director(id=2, name="Director2")
    director_3 = Director(id=3, name="Director3")

    directors_data = {1: director_1, 2: director_2, 3: director_3}

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=directors_data.values())
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name="Genre1")
    genre_2 = Genre(id=2, name="Genre2")
    genre_3 = Genre(id=3, name="Genre3")

    genre_data = {1: genre_1, 2: genre_2, 3: genre_3}

    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = MagicMock(return_value=genre_data.values())
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(id=1, title="Movie1", description="description1", trailer="trailer1",
                    year=2000, rating=10.1, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Movie2", description="description2", trailer="trailer2",
                    year=2001, rating=10.2, genre_id=2, director_id=2)
    movie_3 = Movie(id=3, title="Movie3", description="description3", trailer="trailer3",
                    year=2002, rating=10.3, genre_id=3, director_id=3)

    movie_data = {1: movie_1, 2: movie_2, 3: movie_3}

    movie_dao.get_all = MagicMock(return_value=movie_data.values())
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.create = MagicMock(return_value=movie_1)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao

