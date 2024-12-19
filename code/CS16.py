def celcius_to_fahrenheit(celcius):
    return((celcius*9/5)+32)

celcius=float(input("Enter temperature in celcius: "))
fahrenheit = celcius_to_fahrenheit(celcius)

print(f"{celcius}°C is {fahrenheit}°F")
