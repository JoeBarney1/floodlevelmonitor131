# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """This is a test to ensure that the typical_range_consistent function works.
    We check this by coming up with a set of data for an arbitrary station, giving values for consistent, inconsistent and nonetype ranges.
    We then assert to check that when data is inconsistent or nonetype, the function returns false.
    If data is consistent, the function should assert as true.
    """
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    inconsistentrange = (7, -2.45)
    NoneRange = None
    consistentrange = (-0.9, 1.12)
    river = "River X"
    town = "My Town"
    inconsistentStation = MonitoringStation(s_id, m_id, label, coord, inconsistentrange, river, town)
    NoneStation = MonitoringStation(s_id, m_id, label, coord, NoneRange, river, town)
    consistentStation = MonitoringStation(s_id, m_id, label, coord, consistentrange, river, town)
    assert consistentStation.typical_range_consistent() == True
    assert inconsistentStation.typical_range_consistent() == False
    assert NoneStation.typical_range_consistent() == False


def test_inconsistent_typical_range_stations():
    """This is a test to ensure that the inconsistent_typical_range_stations function works.
    We check this by coming up with a set of data for an arbitrary station, giving values for consistent, inconsistent and nonetype ranges.
    We then assert to check that when data is inconsistent it appears in the list as such, and when data is consistent, it is left out.
    """
    s_id = "test-s-id"
    m_id = "test-m-id"
    label1 = "some inconsistent station"
    label2 = "some consistent station"
    label3 = "some nonetype station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    inconsistentrange = (7, -2.45)
    NoneRange = None
    consistentrange = (-0.9, 1.12)
    inconsistentStation = MonitoringStation(s_id, m_id, label1, coord, inconsistentrange, river, town)
    NoneStation = MonitoringStation(s_id, m_id, label3, coord, NoneRange, river, town)
    consistentStation = MonitoringStation(s_id, m_id, label2, coord, consistentrange, river, town)
    stations = [inconsistentStation, NoneStation, consistentStation]
    assert inconsistentStation.name in inconsistent_typical_range_stations(stations)
    assert consistentStation.name not in inconsistent_typical_range_stations(stations)
    assert NoneStation.name in inconsistent_typical_range_stations(stations)


