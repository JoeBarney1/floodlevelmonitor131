from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""
    stations=build_station_list()
    print(sorted(inconsistent_typical_range_stations(stations)))

if __name__ == "__main__":
    run()