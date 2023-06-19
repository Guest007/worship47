import string
from random import choice

from django.urls import reverse

import pytest
from accounts.models import User
from songs.models import Song


pytestmark = pytest.mark.django_db


def generate_str(length=50, chars=None):
    if not chars:
        chars = string.ascii_uppercase + string.digits
    return "".join(choice(chars) for _ in range(length))


def get_index_url():
    return reverse("home")


def get_song_list_url():
    return reverse("songs-list-first")


def get_song_details_url(song_id):
    return reverse("song-detail", args=[song_id])


def get_song_update_url(song_id):
    return reverse("song-update", args=[song_id])


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


def test_index_url_anonymous(db, client):
    url = get_index_url()
    res = client.get(url)

    assert res.status_code == 200
    assert "Вход/регистрация" in res.rendered_content


def test_index_url_logged_user(db, client, regular_user):
    url = get_index_url()
    client.force_login(regular_user)
    res = client.get(url)

    assert res.status_code == 200
    assert f"Привет, {regular_user.first_name}" in res.rendered_content


def test_songs_list_anonymous(client, empty_song):
    url = get_song_list_url()
    detail_url = get_song_details_url(empty_song.id)
    res = client.get(url)
    assert res.status_code == 200
    assert empty_song.title in res.rendered_content
    assert "Login first" in res.rendered_content
    assert detail_url not in res.rendered_content


def test_songs_list_authenticated(regular_user, client, empty_song):
    url = get_song_list_url()

    client.force_login(regular_user)

    detail_url = get_song_details_url(empty_song.id)

    res = client.get(url)
    assert res.status_code == 200
    assert "Login first" not in res.rendered_content
    assert "edit" not in res.rendered_content
    assert detail_url in res.rendered_content


def test_songs_list_staff(user_factory, client, empty_song):
    url = get_song_list_url()
    user = user_factory(is_staff=True)

    client.force_login(user)

    update_url = get_song_update_url(empty_song.id)

    res = client.get(url)
    assert res.status_code == 200
    assert "edit" in res.rendered_content
    assert update_url in res.rendered_content
