FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
temp_input = float(input("Enter the temperature value: "))

unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

if unit == "C" or unit == "CELSIUS":
        converted = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {converted:.2f}°F")

elif unit == "F" or unit == "FAHRENHEIT":
        converted = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {converted:.2f}°C")

else:
    raise ValueError("Invalid temperature. Please enter a numeric value.")