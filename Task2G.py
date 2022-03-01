from floodsystem.joe_flood import highest_risk
from floodsystem.stationdata import build_station_list
import datetime 
def run():
    """Requirements for Task 2G"""
    stations= build_station_list()
    print(highest_risk(stations))


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()