# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from importlib_metadata import import_module
from haversine import haversine, Unit 
from floodsystem.utils import sorted_by_key# noqa
from floodsystem.stationdata import build_station_list
def stations_by_distance(stations, p): 
    station_distances=[] #empty list for station name and dist from p
    for station in stations:
        distance=float(haversine(p,station.coord)) #set distance for each loop as dist from p
        station_distances += (station.name, distance) #adds a tuple of a station name and it's distance from p to empty list
    sorted_station_distances = sorted_by_key(station_distances, int(1)) #sorts list based on second item i.e distance not name
    return sorted_station_distances
    
def stations_within_radius(stations, centre, r):
    final_list = []
    for tt in stations:
        stloc = tt.coord
        if haversine(stloc, centre) < r:
            final_list.append(tt.name)
    return final_list
