from distutils.command.build import build
from floodsystem.stationdata import update_water_levels
from .station import MonitoringStation
from .utils import sorted_by_key



def stations_level_over_threshold(stations, tol):
    over_limit = []
    for station in stations:
        if (type(station.latest_level) == float)  and (station.typical_range_consistent() == True):
            if (station.relative_water_level() > tol):
                over_limit.append((station, station.relative_water_level()))
    
    sorted_stations = sorted_by_key(over_limit, 1, True)

    return (sorted_stations)
    
