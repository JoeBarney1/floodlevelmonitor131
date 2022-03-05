from distutils.command.build import build
from floodsystem.stationdata import update_water_levels
from .utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, NoneType
import datetime
from .datafetcher import fetch_measure_levels

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


def stations_level_over_threshold(stations, tol):
    over_limit = []
    for station in stations:
        if (type(station.latest_level) == float)  and (station.typical_range_consistent() == True):
            if (station.relative_water_level() > tol):
                over_limit.append((station, station.relative_water_level()))
    
    sorted_stations = sorted_by_key(over_limit, 1, True)

    return (sorted_stations)
    
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
            dates,levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            #finds dates,levels for river over past dt days
            try:
                predicted_rise= (levels[0]-levels[-1])*(y/dt)
            #takes difference between first and last values from levels list,to get change in level over 'dt' days. Then divides by dt for rise per day
            #Then multiplies this diff by the number of days over which the risk levels are to be predicted, to get the predicted rise  
            
            # COULD USE MORE RECENT GRADIENT, which   
            except IndexError:
            #avoids an error when fetch measure levels is an empty list, due to an 'except IndexError' added in the fetch function
                continue
            except TypeError:
            #avoids an error when fetch measure levels[0] or levels[-1] is a list, due to an Error in the fetch function
                continue                 
            predicted_rel_level=round((relative_level + predicted_rise),4)
            #predicted relative level is current level added to expected rise, rounded to 4dp
            if predicted_rel_level>5:
                risk_rating="Severe"
            elif predicted_rel_level<5 and predicted_rel_level>=1:
                risk_rating="High"
            elif predicted_rel_level<1 and predicted_rel_level>=0:
                risk_rating="Moderate"
            elif predicted_rel_level<0:
                risk_rating="Low"
            #applies an arbitrary risk rating based on predicted level
            predicted_levels.append((station.town, "Predicted relative level={}".format(predicted_rel_level) ,"Risk={}".format(risk_rating) ))
            #adds station, its predicted level and its risk rating a tuple to a list
    sorted_predicted_levels= sorted_by_key(predicted_levels, int(1),reverse=True)
    #sorts list based on predicted level, in reverse (to make list descending)
    shortened_list=[]
    #creates empty list 'N' most at risk stations
    for tuple in sorted_predicted_levels[0:N]:
        #iterates over first 'N' tuples in list of (station,predicted level, risk rating)
        shortened_list.append(tuple)
    #adds N tuples of sorted list to a new list
    print("This prediction is based on data over the past {} days, predicting {} days into the future".format(dt,y))
    return seshortened_list

    