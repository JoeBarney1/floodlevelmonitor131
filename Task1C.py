from distutils.command.build import build
from sympy import N
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

print(stations_within_radius(build_station_list(),(52.2053, 0.1218), 10))
