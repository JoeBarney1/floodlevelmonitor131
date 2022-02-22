from sympy import stationary_points
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.joe_flood import plot_water_levels, stations_high_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime
# stations=build_station_list()
# update_water_levels(stations)
# for station in stations:
#     if station.typical_range != None: #and station.latest_level!= None:
#         print(station.typical_range[1])
#         print(station.latest_level)
#         #print(station.typical_range[1]-station.latest_level)
stations=build_station_list()
# s=stations_high_rel_level(stations,5)
dt=10
for station in stations[0:1]:
#     print(fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt)))
    dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
    print (dates)
    print(levels)
# [0]
#         #outputs all dates/times going back 10 days
#         levels=fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))[1]
#         #outputs water levels at each time
#         plot_water_levels(stations,dates,levels)