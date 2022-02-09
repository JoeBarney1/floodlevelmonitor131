# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
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

def stations_within_radius(stations, centre, r):
    final_list = []
    for tt in stations:
        stloc = tt.coord
        if haversine(stloc, centre) < r:
            final_list.append(tt.name)
    return final_list

def rivers_by_station_number(stations, N):
    #Empty lists for the important variables. Num being the overall count for each river, and river_list being the list of all rivers each time it occurs.
    num = []
    river_list = []
    for x in stations:
        #Iterating over every station and appending the name of the river to a list.
        river_list.append(x.river)
    for r in river_list:
        #Iterating over the river list and counting the number of times the river appears.
        c = river_list.count(r)
        num.append((r,c))
    # As the above method involves river names and counts being repeated multiple times, converting to a dictionary then back to list removes duplicates.
    num = list(dict.fromkeys(num))
    #Sorting the list by the second value of the tuple - the frequency.
    num.sort(key=lambda x:x[1], reverse=True)
    # A new list is the sliced version of the previous one, only showing the first N numbers.
    while num[N-1][1] == num[N][1]:
        N += 1
    numN = num[0:N]
    return numN