from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, NoneType
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
import matplotlib.pyplot as plt
import datetime 
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np

#Task 2C
def stations_highest_rel_level(stations,N):
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


#task 2E
def plot_water_levels(station, dates, levels):

    t =dates
    level = levels
    # Plot
    plt.plot(t, level)
    


    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Station {}".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    if station.typical_range != None:
            plt.axhline(station.typical_range[0], color='r') # lower level
            plt.axhline(station.typical_range[1], color='r') # upper level
    plt.show()

#function which calculates predicted overflowing level in a week based on current data
#use effectively v. simple numerical integration, find relative level at some point, plus difference between current level and a few days ago,
# then find predicted relative level in next few days, adn rank using similar code to that in 1C  

#Task 2G
def highest_risk(stations,dt=3,N=10,y=3):
    """calculates relative risk level compared to its typical range, and 'predicted' level based on rise over past 'dt' days. Predicts 'y' days into future, returns 'N' highest"""
    predicted_levels=[] 
    #creates an empty list
    update_water_levels(stations)
    for station in stations:
        if station.typical_range != None and station.typical_range_consistent and station.latest_level !=None:
        #makes sure it only counts stations with consistent data
            relative_level=station.latest_level-station.typical_range[1]
            #finds difference between current station level and typical upper range
            k=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            try:
                predicted_rise= (k[1][0]-k[1][-1])*(int(y/dt))
            except IndexError:
                continue
            except TypeError:
                continue
            #takes difference between first and last values from second list of fetch measure levels funct, giving change in level over 'dt' days
            #Then multiplies this diff by the number of days over which the risk levels are to be predicted, to get the predicted rise                      
            predicted_rel_level=round((relative_level + predicted_rise),4)
            if predicted_rel_level>5:
                risk_rating="Severe"
            elif predicted_rel_level<5 and predicted_rel_level>=1:
                risk_rating="High"
            elif predicted_rel_level<1 and predicted_rel_level>=0:
                risk_rating="Moderate"
            elif predicted_rel_level<0:
                risk_rating="Low"
            predicted_levels.append((station.name, "Predicted relative level={}".format(predicted_rel_level) ,"Risk={}".format(risk_rating) ))
            #adds station, its predicted level and its risk rating a tuple to a list
    sorted_predicted_levels= sorted_by_key(predicted_levels, int(1),reverse=True)
    #sorts list based on predicted level, in reverse (to make list descending)
    shortened_list=[]
    #creates empty list 'N' most at risk stations
    for tuple in sorted_predicted_levels[0:N]:
        #iterates over first 'N' tuples in list of (station,predicted level, risk rating)
        shortened_list.append(tuple)
    #adds N tuples of sorted list to a new list
    return shortened_list

    
    
