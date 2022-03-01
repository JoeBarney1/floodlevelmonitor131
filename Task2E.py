import datetime
from floodsystem.joe_flood import plot_water_levels, stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():
    stations=build_station_list()
    s=stations_highest_rel_level(stations,5)
    #gets top 5 relative levelled stations
    dt = 10
    for station in s:
        #iterates over each station and plots a graph using dates+levels for each one
        dates, levels = fetch_measure_levels(station.measure_id,dt=datetime.timedelta(days=dt))
        plot_water_levels(station,dates,levels)




if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()