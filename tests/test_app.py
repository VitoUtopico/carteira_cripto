from tests import url_prefix
from pytest import mark

def test_app_is_created(app):
    assert app.name == "carteira_cripto.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False

@mark.get_request
@mark.parametrize(
    'route, expected_status_code',
    [
        (f'{url_prefix}/price/bitcoin,cardano/brl', 200),
        (f'{url_prefix}/calcs/', 405)
    ])
def test_if_get_requests_returns_expected_status_code(client, route, expected_status_code):
    assert client.get(route) == expected_status_code
    
@mark.post_request
@mark.parametrize(
    'route, expected_status_code',
    [
        (f'{url_prefix}/price/bitcoin,cardano/brl', 405),
        (f'{url_prefix}/calcs/', 200)
    ])
def test_if_post_requests_returns_expected_status_code(client, route, expected_status_code):
    assert client.post(route) == expected_status_code

