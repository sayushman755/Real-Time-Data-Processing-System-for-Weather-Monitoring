# Weather Monitoring System

This application continuously retrieves weather data for major Indian metros and provides daily summaries along with configurable alerts.

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourhandle/weather-monitoring.git
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app/weather_data.py
```

Alternatively, you can build and run the Docker container:
```bash
docker build -t weather-monitoring .
docker run -d weather-monitoring
```

## Design Choices
- **API Integration**: The system retrieves data using the OpenWeatherMap API and processes it at regular intervals.
- **Temperature Conversion**: Converts temperature from Kelvin to Celsius/Fahrenheit based on user preference.
- **Rollups and Aggregates**: Provides daily summaries with average, max, min temperatures, and dominant weather conditions.
