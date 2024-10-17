def check_threshold_breach(temp, threshold):
    """Check if a threshold is breached"""
    return temp > threshold

def monitor_alerts(weather_data, threshold):
    """Continuously monitor for alerts when a threshold is breached"""
    alerts = []
    for city, data in weather_data.items():
        temp = data['main']['temp']
        if check_threshold_breach(temp, threshold):
            alerts.append(f"Alert! Temperature in {city} exceeds {threshold}°C")
    return alerts
