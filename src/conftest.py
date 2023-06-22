import string
from random import choice

import pytest
from accounts.models import User
from songs.models import Song


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


def generate_str(length=50, chars=None):
    if not chars:
        chars = string.ascii_uppercase + string.digits
    return "".join(choice(chars) for _ in range(length))


@pytest.fixture
def user_factory():
    def _inner(first_name="", email="", is_staff=False):
        user = User.objects.create(
            first_name=first_name if first_name else "first_name",
            email=email if email else "test@example.com",
            is_staff=is_staff,
        )
        return user

    return _inner


@pytest.fixture
def regular_user(user_factory):
    return user_factory()


@pytest.fixture
def song_factory():
    def _inner(title=""):
        song = Song.objects.create(
            title=title if title else generate_str(),
        )
        return song

    return _inner


@pytest.fixture
def empty_song(song_factory):
    return song_factory()
