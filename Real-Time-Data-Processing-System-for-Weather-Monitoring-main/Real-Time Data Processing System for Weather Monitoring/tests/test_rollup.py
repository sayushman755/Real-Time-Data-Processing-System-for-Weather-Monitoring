import pytest
from app.rollup_aggregates import calculate_daily_summary

def test_calculate_daily_summary():
    weather_data = [ # Sample data
        {'main': {'temp': 300}, 'weather': [{'main': 'Clear'}]},
        {'main': {'temp': 302}, 'weather': [{'main': 'Clear'}]},
        {'main': {'temp': 298}, 'weather': [{'main': 'Rain'}]},
    ]
    summary = calculate_daily_summary(weather_data)
    assert summary['average_temp'] == 300.0
    assert summary['max_temp'] == 302
    assert summary['min_temp'] == 298
    assert summary['dominant_condition'] == 'Clear'
