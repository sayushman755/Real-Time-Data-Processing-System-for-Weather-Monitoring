import pytest
from app.temperature_conversion import convert_temperature

def test_kelvin_to_celsius():
    assert convert_temperature(300, 'C') == 26.85

def test_kelvin_to_fahrenheit():
    assert convert_temperature(300, 'F') == 80.33
