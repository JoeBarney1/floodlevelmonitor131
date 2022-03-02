from floodsystem.joe_flood import highest_risk
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 2G"""
    stations= build_station_list()
    print(highest_risk(stations,dt=3,N=10,y=3))
    #works with whole list but takes v. long time


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()