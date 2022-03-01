from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, NoneType
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

#Plan for Task 2C
def stations_high_rel_level(stations,N):
    """calculates relative water level compared to its typical range, returns 'N' highest"""
    relative_levels=[] 
    #creates an empty list
    update_water_levels(stations)
    for station in stations:
        if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None :
            #only counts stations with consistent data
            relative_level=station.latest_level-station.typical_range[1]
            #finds difference between current station level and typical upper range
            relative_levels.append((station,relative_level))
            #adds station and its relative level as a tuple to a list
    sorted_relative_levels= sorted_by_key(relative_levels, int(1),reverse=True)
    #sorts list based on relative level, in reverse (to make list descending)
    station_only=[]
    #creates empty list for just stations
    for tuple in sorted_relative_levels[0:N]:
        #iterates over first 'N' tuples in list of (station,relative level)
        station_only.append(tuple[0])
    #adds station terms of sorted list to a new list
    return station_only


#Plan for task 2E
def plot_water_levels(station, dates, levels):

    t =dates
    level = levels
    # Plot
    plt.plot(t, level)
    


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station {}".format(station))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    if station.typical_range != None:
            plt.axhline(station.typical_range[0], color='r') # lower level
            plt.axhline(station.typical_range[1], color='r') # upper level
    plt.show()

#plan for task 2G
#function which calculates predicted overflowing level in a week based on current data
#use effectively v. simple numerical integration, find relative level at some point, plus difference between current level and a few days ago,
# then find predicted relative level in next few days, adn rank using similar code to that in 1C  

    
    
