def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(kelvin, preference='C'):
    """Convert temperature based on user preference"""
    if preference == 'F':
        return kelvin_to_fahrenheit(kelvin)
    return kelvin_to_celsius(kelvin)
