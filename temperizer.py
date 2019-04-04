"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    return (temperature_c*1.8)+32

def convert_c_to_k(temp_c):
    temp_k = temp_c + 273.15
    return temp_k if temp_k >= 0 else "Can't be colder than absolute zero."

def convert_f_to_k(temp_f):
    return convert_c_to_k(convert_f_to_c(temp_f))

def convert_k_to_c(temp_k):
    temp_c = temp_k - 273.15
    return temp_c if temp_c >= -273.15 else "Can't be colder than absolute zero."

def convert_k_to_f(temp_k):
    try:
        return convert_c_to_f(convert_k_to_c(temp_k)) 
    except:
        return "Can't be colder than absolute zero."