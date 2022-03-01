from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stationlist = build_station_list()
    update_water_levels(stationlist)
    over_limit = stations_level_over_threshold(stationlist, 0.8)
    for x in range (len(over_limit)):
        print (str(over_limit[x][0].name), str(over_limit[x][1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()