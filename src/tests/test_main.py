credentials = {
    "login": "spidermind",
    "password": "lolkekcheburek"
}

wrong_credentials = {
    "login": "spidermind",
    "password": "password"
}

def test_login(test_app):
    response = test_app.post("/token", json=credentials)
    assert response.status_code == 200
    assert response.json() == 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2Nlc3NfdG9rZW4iOiJzcGlkZXJtaW5kIiwidG9rZW5fdHlwZSI6ImJlYXJlciJ9.epJcNkwzHUfuwRDHk2rA43SxHPQjqJKht8YlY-LqD8w'

def test_login_wrong(test_app):
    response = test_app.post("/token", json=wrong_credentials)
    assert response.status_code == 400
    assert response.json() == {'detail': 'Incorrect username or password'}

def test_login_nodata(test_app):
    response = test_app.post("/token")
    assert response.status_code == 422




