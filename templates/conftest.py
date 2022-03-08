"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
import app


@pytest.fixture()
def application():
    """This makes the app"""
    application = app.create_app()
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()