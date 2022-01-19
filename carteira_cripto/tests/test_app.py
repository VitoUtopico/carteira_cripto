def test_app_is_created(app):
    assert app.name == "carteira_cripto.app"


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_api_coingecko(client):
    response = client.get('/price/bitcoin,cardano/brl')
    assert response.status_code == 200
    data = response.json['bitcoin']
    
