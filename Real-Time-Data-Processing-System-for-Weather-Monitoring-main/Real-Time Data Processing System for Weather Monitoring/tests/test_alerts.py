import pytest
from app.alerts import monitor_alerts

def test_monitor_alerts():
    weather_data = {
        'Delhi': {'main': {'temp': 36}},
        'Mumbai': {'main': {'temp': 34}},
    }
    alerts = monitor_alerts(weather_data, 35)
    assert alerts == ["Alert! Temperature in Delhi exceeds 35°C"]
