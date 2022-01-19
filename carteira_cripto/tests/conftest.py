import pytest

from carteira_cripto.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    return create_app()
