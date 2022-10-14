import json
import sys
import pytest

sys.path.append('/Users/christian/Desktop/joan_proj/coding_test/')
from weather_collector import WeatherCollector

# Test for Salt Lake City, Utah

file = open('mock_data/mock_data.json', 'r')
data = json.load(file)
w = WeatherCollector()

def test_temperature():
    # test 1: test if average temperature is returning an float
    temp = w.get_temperature(data=data)
    assert type(temp) == float

def test_no_periods():
    # test 2: test if error message is correct if there is no periods
    test_data = data.copy()
    test_data['properties']['periods'] = None
    temp = w.get_temperature(data=test_data)
    assert temp == 'No periods available '

def test_no_properties():
    # test 3: test if error message is correct if there is no properties
    test_data = data.copy()
    test_data = None
    temp = w.get_temperature(data=test_data)
    assert temp == 'No properties available '

def test_location():
    # test 4: test if location is returning a dictionary
    w.get_location(data=data)
    assert type(w.location.raw) == dict

def test_no_coordinates():
    # test 5: test if error message is correct if there is no coordinates
    test_data = data.copy()
    test_data['geometry'] = None
    loc = w.get_location(data=test_data)
    assert loc == 'No coordinates available '

def test_no_geometry():
    # test 6: test if error message is correct if there is no geometry
    test_data = data.copy()
    test_data = None
    loc = w.get_location(data=test_data)
    assert loc == 'No geometry available '