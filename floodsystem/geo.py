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
