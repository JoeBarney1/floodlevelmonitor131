from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.utils import sorted_by_key

def stations_high_rel_level(stations,N):
    """calculates relative water level compared to its typical range, returns 'N' highest"""
    relative_levels=[] 
    #creates an empty list
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
    return station_only

    
    
    
    
