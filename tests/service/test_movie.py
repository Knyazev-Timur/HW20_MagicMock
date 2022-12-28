from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title="Броненосец Потемкин",
        description="Сюжет, основанный на подлинном историческом событии, образно выразил основные социальные тенденции ХХ века: "
                    "массовое стремление к свободе, борьбу с тиранией, защиту человеческого достоинства, призыв к единению людей во имя равноправия. "
                    "Новаторская форма фильма и сегодня оказывает глубокое влияние на развитие выразительных средств кино.",
        trailer='https://www.kinopoisk.ru/film/481/',
        year=1925,
        rating=1.0,
        genre_id=1,
        director_id=1
    )

    movie_2 = Movie(
        id=2,
        title="Дорога",
        description="Фильм о нечеловеческой жестокости и человеческом страдании, о непростых отношениях немножко сумасшедшей, "
                    "немножко святой, взъерошенной, смешной, неуклюжей и нежной Джельсомины и мрачного, массивного, "
                    "грубого и звероподобного Дзампано - женщины и мужчины, совершенно чуждых друг другу, но волею судеб, неизвестно почему, оказавшихся вместе...",
        trailer="https://www.kinopoisk.ru/film/531/",
        year=1954,
        rating=18.0,
        genre_id=2,
        director_id=2
    )

    movie_3 = Movie(
        id=3,
        title="Андеграунд",
        description="Во время Второй мировой войны в Белграде подпольщики-антифашисты организовали целую фабрику по производству оружия."
                    " Война давно закончилась, а они продолжают свою деятельность. И все эти годы наверху жизнь течёт своим чередом, "
                    "а в подполье рождаются дети, которые никогда не видели солнечного света.",
        trailer="https://www.kinopoisk.ru/film/7698/",
        year=1995,
        rating=16.0,
        genre_id=2,
        director_id=3
    )

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies)> 0

    def test_create_movie(self):
        create_movie = {
            'id': 1,
            'title': 'Броненосец «Потемкин»',
            'description': 'Сюжет, основанный на подлинном историческом событии, '
        'образно выразил основные социальные тенденции ХХ века: '
        'массовое стремление к свободе, борьбу с тиранией, защиту человеческого достоинства, '
        'призыв к единению людей во имя равноправия. Новаторская форма фильма и сегодня оказывает глубокое '
        'влияние на развитие выразительных средств кино.',
            'trailer': 'https://www.kinopoisk.ru/film/481/',
            'year': '1925',
            'rating': 1.0,
            'genre_id': 1,
            'director_id': 1
        }
        movie = self.movie_service.create(create_movie)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)


    def test_update(self):
        movie_update = {
            'id': 1,
            'title': 'Броненосец «Потемкин»',
            'description': 'Сюжет, основанный на подлинном историческом событии, '
        'образно выразил основные социальные тенденции ХХ века: '
        'массовое стремление к свободе, борьбу с тиранией, защиту человеческого достоинства, '
        'призыв к единению людей во имя равноправия. Новаторская форма фильма и сегодня оказывает глубокое '
        'влияние на развитие выразительных средств кино.',
            'trailer': 'https://www.kinopoisk.ru/film/481/',
            'year': '1925',
            'rating': 12.0,
            'genre_id': 1,
            'director_id': 1
        }
        self.movie_service.update(movie_update)
