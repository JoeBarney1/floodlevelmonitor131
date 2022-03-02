from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation, NoneType
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import update_water_levels
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from .analysis import polyfit
import numpy as np
import matplotlib.dates as da
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

def plot_water_level_with_fit(station, dates, levels, p):
        poly, d0 = polyfit(dates, levels, p)
        plt.plot(dates, levels)
        dates_floats = da.date2num(dates)
        plt.plot(dates, poly(dates_floats - dates_floats[0]), color='g')
        if station.typical_range_consistent():
                plt.axhline(y = station.typical_range[0], color = 'r', linestyle = '-')
                plt.axhline(y = station.typical_range[1], color = 'r', linestyle = '-')
        plt.xlabel('Date')
        plt.title(station.name)
        plt.xticks(rotation=45)
        plt.ylabel('Water Level (m)')
        plt.tight_layout()
        plt.show()