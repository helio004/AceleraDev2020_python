from main import get_temperature


def test_get_temperature_by_lat_lng():

    lat = -14.235004
    lng = -51.92528

    temp = get_temperature(lat, lng)
    return temp == 16
