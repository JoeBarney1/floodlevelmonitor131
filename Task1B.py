from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
def run():
    stations=build_station_list()
    distancefromcam= stations_by_distance(stations,(52.2053, 0.1218))
    closest= distancefromcam[:10]
    furthest = distancefromcam[-10:]
    print(closest) 
    print(furthest) 

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()