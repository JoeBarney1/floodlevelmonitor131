from sympy import stationary_points
from floodsystem.stationdata import build_station_list, update_water_levels

stations=build_station_list()
update_water_levels(stations)
for station in stations:
    if station.typical_range != None: #and station.latest_level!= None:
        print(station.typical_range[1])
        print(station.latest_level)
        #print(station.typical_range[1]-station.latest_level)