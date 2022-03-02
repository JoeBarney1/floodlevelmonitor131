from distutils.command.build import build
from floodsystem.stationdata import update_water_levels
from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, NoneType


def stations_high_rel_level(stations,N):
    """calculates relative water level compared to its typical range, returns 'N' highest"""
    relative_levels=[] 
    #creates an empty list
    update_water_levels(stations)
    for station in stations:
        if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None :
            #only counts stations with consistent data
            relative_level=station.latest_level-station.typical_range[1]
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


def stations_level_over_threshold(stations, tol):
    over_limit = []
    for station in stations:
        if (type(station.latest_level) == float)  and (station.typical_range_consistent() == True):
            if (station.relative_water_level() > tol):
                over_limit.append((station, station.relative_water_level()))
    
    sorted_stations = sorted_by_key(over_limit, 1, True)

    return (sorted_stations)
    
