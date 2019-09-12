from main import get_temperature

import requests
import pytest

'''
lat = -14.235004
lng = -51.92528
temperature = 62
expected = 16
'''

# Classe para retornar o valor mockado
# Ele sobrescreve o requests.Response que é retornado pelo requests.get
class MockResponse:

    @staticmethod
    def json():
        return {"currently": {"temperature": 62}}


#@pytest.mark.parametrize('lat, lng, expected', [(-14.235004,-51.92528,16)])  # Setup 
@pytest.mark.parametrize('lat', [-14.235004])  # Setup 
@pytest.mark.parametrize('lng', [-51.92528])  # Setup 
@pytest.mark.parametrize('expected', [16])  # Setup 
def test_get_temperature_by_lat_lng(monkeypatch, lat, lng, expected):

    # Mock_get sempre vai retornar o objeto do metodo json()
    def mock_get(*args, **kwargs):
        return MockResponse()

    # Usa o monkeypatch para a requisição requests.get no mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    # Execução do teste
    result = get_temperature(lat, lng)

    # Verificação do resultado do teste
    assert result is expected