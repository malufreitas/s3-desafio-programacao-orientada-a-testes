from main import get_temperature

def test_get_temperature_by_lat_lng():
    # Setup
    lat = -14.235004
    lng = -51.92528
    temperature = 62
    expected = 16

    # Execução do teste
    resp = get_temperature(lat, lng)

    # Verificação do resultado do teste
    assert resp is expected