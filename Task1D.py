from importlib_metadata import import_module
from haversine import haversine, Unit 
from floodsystem.utils import sorted_by_key# noqa
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
def run():
    stations=build_station_list() #creates list of all station objects
    rivers_with_station(stations) #uses function to create list of all rivers with a station
    rivers_sorted=sorted(rivers_with_station(stations)) #sorts alphabetically
    print(len(rivers_sorted)) #prints no. of stations
    print(rivers_sorted[0:10]) #prints first 10 rivers
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations) #creates dictionary with all rivers as key
    # print(rivers_dict)  
    print("River Aire:")
    print(sorted(rivers_dict['River Aire']))
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations) #creates dictionary with all rivers as key
    # print(rivers_dict)  
    print("River Cam:")
    print(sorted(rivers_dict['River Cam']))  
    print("""
    *
    *
    *""")

    rivers_dict=stations_by_river(stations) #creates dictionary with all rivers as key
    # print(rivers_dict)  
    print("River Thames:")
    print(sorted(rivers_dict['River Thames']))  

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

