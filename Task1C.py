from distutils.command.build import build
from sympy import N
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


cam = (52.2053, 0.1218)
print(stations_within_radius(build_station_list(),cam, 10))
