from typing import List
from sympy import stationary_points
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.joe_flood import plot_water_levels, stations_highest_rel_level
from floodsystem.datafetcher import fetch, fetch_measure_levels
from floodsystem.stationdata import build_station_list
import datetime
from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.joe_flood import highest_risk
# stations=build_station_list()
# update_water_levels(stations)
# for station in stations:
#     if station.typical_range != None: #and station.latest_level!= None:
#         print(station.typical_range[1])
#         print(station.latest_level)
#         #print(station.typical_range[1]-station.latest_level)
# stations=build_station_list()
# # s=stations_high_rel_level(stations,5)
# dt=10
# for station in stations[0:1]:
# #     print(fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt)))
#     dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
#     print (dates)
#     print(levels)
# [0]
#         #outputs all dates/times going back 10 days
#         levels=fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))[1]
#         #outputs water levels at each time
#         plot_water_levels(stations,dates,levels)
# stations = build_station_list()
# dt=5
# station=stations[1]
# # dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
# # plot_water_levels(station,dates,levels)
# # print(fetch_measure_levels(stations[1].measure_id,dt=datetime.timedelta(days=dt)))
# print(fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))[1][0]-fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))[1][-1])
# for s in stations:
#     if s.name[0:3]=="Let":
#         print(s)

# def run():
#     """Requirements for Task 2C"""
#     stations= build_station_list()
#     for s in stations_high_rel_level(stations,10):
#         relative_level=s.latest_level-s.typical_range[1]
#         print(s.name, relative_level)
#Task 2G

# def highest_risk(stations,dt=3,N=10,y=3):
#     """calculates relative risk level compared to its typical range, and 'predicted' level based on rise over past 'dt' days. Predicts 'y' days into future, returns 'N' highest"""
#     predicted_levels=[] 
#     #creates an empty list
#     update_water_levels(stations)
#     for station in stations:
#         if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None:
#         #makes sure it only counts stations with consistent data
#             relative_level=station.latest_level-station.typical_range[1]
#             #finds difference between current station level and typical upper range
#             try:
#                 predicted_rise=(fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))[1][0]-fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))[1][-1])*(y/dt)
#         #takes difference between first and last values from second list of fetch measure levels funct, giving change in level over 'dt' days
#         #Then multiplies this diff by the number of days over which the risk levels are to be predicted, to get the predicted rise
#             except IndexError:
#                 continue                        
#         predicted_rel_level=relative_level + predicted_rise
#         if predicted_rel_level>5:
#             risk_rating="Severe"
#         elif predicted_rel_level<5 and predicted_rel_level>=1:
#             risk_rating="High"
#         elif predicted_rel_level<1 and predicted_rel_level>=0:
#             risk_rating="Moderate"
#         elif predicted_rel_level<0:
#             risk_rating="Low"
#         predicted_levels.append((station.name,predicted_rel_level,"Risk={}".format(risk_rating)))
#         #adds station, its predicted level and its risk rating a tuple to a list
#     sorted_predicted_levels= sorted_by_key(predicted_levels, int(1),reverse=True)
#     #sorts list based on predicted level, in reverse (to make list descending)
#     shortened_list=[]
#     #creates empty list 'N' most at risk stations
#     for tuple in sorted_predicted_levels[0:N]:
#         #iterates over first 'N' tuples in list of (station,predicted level, risk rating)
#         shortened_list.append(tuple)
#     #adds N tuples of sorted list to a new list
#     return shortened_list
stations=build_station_list()
dt=1
    #k=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
print(highest_risk(stations[0:200], dt=1,N=3,y=2))
    # try:
        # if type(k[1][0]) == 'list' or type(k[1][-1])=='list':
        #     print(k[1][0], k[1][-1])
    #     if type([1, 3, 4]) is list:
    #         print(type([1, 3, 4]))
    #         print([1, 3, 4])
    # except IndexError:
    #     continue

