from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.joe_flood import stations_high_rel_level
from floodsystem.utils import sorted_by_key


# def run():
#     """Requirements for Task 2C"""
#     stations= build_station_list()
#     print(stations_high_rel_level(stations,10))


# if __name__ == "__main__":
#     print("*** Task 2C: CUED Part IA Flood Warning System ***")
#     run()
relative_levels=[] 
    #creates an empty list
stations= build_station_list()
for station in stations:
        relative_level=station.typical_range[1]-station.latest_level
        #finds difference between current station level and typical upper range
        relative_levels.append((station,relative_level))
        #adds station and its relative level as a tuple to a list
sorted_relative_levels= sorted_by_key(relative_levels, int(1),reverse=True)
#sorts list based on relative level, in reverse (to make list descending)
station_only=[]
#creates empty list for just stations
for tuple in sorted_relative_levels[0:N]:
    #iterates over first 'N' tuples in list of (station,relative level)
    station_only.append(tuple[0])
#adds station terms of sorted list to a new list
print(station_only)