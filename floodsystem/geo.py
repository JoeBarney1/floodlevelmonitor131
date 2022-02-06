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
        station_distances.append((station.name, distance)) #adds a tuple of a station name and it's distance from p to empty list
    sorted_station_distances = sorted_by_key(station_distances, int(1)) #sorts list based on second item i.e distance not name
    return sorted_station_distances
    

def rivers_with_station(stations):
    list_rivers=[] 
    for station in stations: #iterates over all the station objects in the given list
        list_rivers.append(station.river) #add each river to the list
    set_rivers=set(list_rivers) #removes duplicate rivers
    return set_rivers

def stations_by_river(stations):
    dict_rivers={} #creates empty dictionary
    for station in stations:#iterates over all the station objects in the given list
        if station.river in dict_rivers.keys(): #checks to see if river is already in dictionary
            dict_rivers[station.river].append(station.name) #adds new station name if river has already been added as a key
        else:
            dict_rivers[station.river]=[station.name] #creates new river key if river isn't in dictionary
    return dict_rivers