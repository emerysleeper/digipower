from tests.data import *


def test_login(test_app):
    response = test_app.post("/login", json=credentials)
    assert response.status_code == 200
    assert response.json() == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NfdG9rZW4iOiJzcGlkZXJtaW5kIiwidG9rZW5fdHlwZSI6ImJlYXJlciJ9.epJcNkwzHUfuwRDHk2rA43SxHPQjqJKht8YlY-LqD8w'


def test_login_wrong(test_app):
    response = test_app.post("/login", json=wrong_credentials)
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect username or password'}


def test_login_nodata(test_app):
    response = test_app.post("/login")
    assert response.status_code == 422


def test_avatar(test_app):
    headers = {'Authorization': correct_token}
    response = test_app.post("/avatar", headers=headers)
    assert response.status_code == 200
    assert response.json() == image


def test_avatar_wrong_token(test_app):
    headers = {'Authorization': incorrect_token}
    response = test_app.post("/avatar", headers=headers)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Incorrect token provided'}


def test_avatar_nodata(test_app):
    response = test_app.post("/avatar")
    assert response.status_code == 403
    assert response.json() == {'detail': 'Incorrect token provided'}


def test_avatar_any(test_app):
    json_data = {'img_string': 'kek'}
    headers = {'Authorization': correct_token}
    response = test_app.post("/avatar/any", headers=headers, json=json_data)
    assert response.status_code == 200
    assert response.json() == image_kek


def test_avatar_any_wrong_token(test_app):
    json_data = {'img_string': 'kek'}
    headers = {'Authorization': incorrect_token}
    response = test_app.post("/avatar/any", headers=headers, json=json_data)
    assert response.status_code == 403
    assert response.json() == {'detail': 'Incorrect token provided'}


def test_avatar_any_small_string(test_app):
    json_data = {'img_string': 'ke'}
    headers = {'Authorization': correct_token}
    response = test_app.post("/avatar/any", headers=headers, json=json_data)
    assert response.status_code == 422


def test_avatar_any_big_string(test_app):
    json_data = {'img_string': 'kekekekekekekekekekekekekekekekekekekekekekekeke'}
    headers = {'Authorization': correct_token}
    response = test_app.post("/avatar/any", headers=headers, json=json_data)
    assert response.status_code == 422


def test_avatar_any_nodata(test_app):
    headers = {'Authorization': correct_token}
    response = test_app.post("/avatar/any", headers=headers)
    assert response.status_code == 422




