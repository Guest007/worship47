from django.urls import reverse


def get_index_url():
    return reverse("home")


def get_song_list_url():
    return reverse("songs-list-first")


def get_api_song_list_url():
    return reverse("api-songs:song-list")


def get_song_details_url(song_id):
    return reverse("song-detail", args=[song_id])


def get_song_update_url(song_id):
    return reverse("song-update", args=[song_id])


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


def test_api_songs_list_authenticated(regular_user, client, empty_song):
    url = get_api_song_list_url()

    client.force_login(regular_user)

    res = client.get(url)

    result_data = res.json()

    assert res.status_code == 200
    assert result_data["count"] == 1


def test_songs_list_staff(user_factory, client, empty_song):
    url = get_song_list_url()
    user = user_factory(is_staff=True)

    client.force_login(user)

    update_url = get_song_update_url(empty_song.id)

    res = client.get(url)
    assert res.status_code == 200
    assert "edit" in res.rendered_content
    assert update_url in res.rendered_content
