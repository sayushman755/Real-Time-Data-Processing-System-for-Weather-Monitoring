import statistics

def calculate_daily_summary(weather_data):
    """Compute the daily summary including average, max, min temperature"""
    temperatures = [entry['main']['temp'] for entry in weather_data]
    
    avg_temp = statistics.mean(temperatures)
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    
    # Determining the dominant weather condition
    weather_conditions = [entry['weather'][0]['main'] for entry in weather_data]
    dominant_condition = max(set(weather_conditions), key=weather_conditions.count)
    
    return {
        "average_temp": avg_temp,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "dominant_condition": dominant_condition
    }
