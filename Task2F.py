from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot_louis import plot_water_level_with_fit
from datetime import timedelta

def run():
    stations = build_station_list()
    update_water_levels(stations)
    for station in stations:
        if station.latest_level is None:
            station.latest_level = -20
    stations.sort(reverse=True, key=lambda x: x.latest_level)
    top5 = stations[:6]
    for station in top5:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days=2))
        if len(dates) > 0:
            plot_water_level_with_fit(station, dates, levels, 4)

if __name__ == "__main__":
    run()