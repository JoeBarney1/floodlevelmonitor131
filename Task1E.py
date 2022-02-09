from distutils.command.build import build
from sympy import N
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    print(rivers_by_station_number(build_station_list(), 9))

if __name__ == "__main__":
    run()