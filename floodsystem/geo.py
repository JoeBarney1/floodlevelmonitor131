# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from importlib_metadata import import_module
from .utils import sorted_by_key  # noqa
from floodsystem.stationdata import build_station_list
import haversine
def stations_by_distance(stations, p):
    stations= build_station_list()
    station_distances=[]
    for station in stations:
        distance=float(haversine(p,))
        station_distances += (station, distance)
