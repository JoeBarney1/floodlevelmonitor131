from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

def test_stations_within_radius():
    """This is a test to ensure that the stations_within_radius function works.
    The representative data shows that, with these coordinates and this radius, there should be 11 stations within radius.
    """
    stations = build_station_list()
    in_radius = geo.stations_within_radius(stations, (52.2053, 0.1218), 10)
    assert len(in_radius) == 11

def test_rivers_with_station():
    """This is a test to ensure that the rivers_with_station function works.
    The assert checks that there aren't more rivers than stations, which wouldn't make any sense.
    The assert also checks that the rivers in the list more than once.
    """
    stations = build_station_list()
    rivers = geo.rivers_with_station(stations)
    assert len(rivers) < len(stations)
    assert type(rivers) == set

def test_stations_by_river():
    """This is a test to ensure that the stations_by_river function works.
    This ensures that the data is placed within a dictionary.
    """
    stations = build_station_list()
    stationsbyriver = geo.stations_by_river(stations)
    assert type(stationsbyriver) == dict

def test_rivers_by_station_number():
    """This is a test to ensure that the rivers_by_station_number function works.
    This ensures that the first value of data in the list is greater than the second value. 
    """
    stations = build_station_list()
    riversbynumber = geo.rivers_by_station_number(stations, 9)
    assert riversbynumber[0][1] > riversbynumber[1][1]
