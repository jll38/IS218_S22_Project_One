"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/">Home</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/python">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data


def test_request_git(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404