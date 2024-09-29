FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """A function to convert fahrenheit to celsius"""
    result = (fahrenheit - 32)  * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}F is {result}C")

def convert_to_fahrenheit(celsius):
    """A function to convert fahrenheit to celsius"""
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}C is {result}F")

temp = input("Enter the temperature to convert: ")

# TRY AND EXCEPT BLOCK
try:
    temp = float(temp)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if unit.lower() == "f":
        convert_to_celsius(temp)
    elif unit.lower == "c":
        convert_to_fahrenheit(temp)
    else:
        print("Not a valid conversion unit")
except ValueError:
    print("Invalid temperature. Please enter a numeric value")
