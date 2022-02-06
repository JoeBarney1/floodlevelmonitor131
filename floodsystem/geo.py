# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa

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
