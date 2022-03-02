import floodsystem.flood as flood
from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list, update_water_levels


def test_stations_over_threshold():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    inconsistentRange = (2.3, -3.4445)
    NoneRange = None
    river = "River X"
    town = "My Town"

    inconsistentStation =  MonitoringStation(s_id, m_id, label, coord, inconsistentRange, river, town)
    NoneStation =  MonitoringStation(s_id, m_id, label, coord, NoneRange, river, town)
    assert flood.stations_level_over_threshold([inconsistentStation, NoneStation], 0.5) == []

    Station1 =  MonitoringStation(s_id, m_id, label, coord, (0, 1), river, town)
    Station2 =  MonitoringStation(s_id, m_id, label, coord, (0.5, 1), river, town)
    Station3 =  MonitoringStation(s_id, m_id, label, coord, (-2, 1.5), river, town)
    
    Station1.latest_level = 0.2
    Station2.latest_level = 0.2
    Station3.latest_level = 0.2
    assert flood.stations_level_over_threshold([Station1, Station2, Station3], -1000) == [(Station3, Station3.relative_water_level()), (Station1, Station1.relative_water_level()), (Station2, Station2.relative_water_level())]
    assert flood.stations_level_over_threshold([Station3, Station2, Station1], 0) == [(Station3, Station3.relative_water_level()), (Station1, Station1.relative_water_level())]
    assert flood.stations_level_over_threshold([Station2, Station1, Station3], 0.21) == [(Station3, Station3.relative_water_level())]
    assert flood.stations_level_over_threshold([Station1, Station3, Station2], 1) == []