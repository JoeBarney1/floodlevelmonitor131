from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.flood import stations_highest_rel_level
from floodsystem.utils import sorted_by_key


def run():
    """Requirements for Task 2C"""
    stations= build_station_list()
    for s in stations_highest_rel_level(stations,10):
        relative_level=s.latest_level-s.typical_range[1]
        print(s.name, relative_level)
    


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
