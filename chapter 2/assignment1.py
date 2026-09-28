# take input in celcius and print its equivalent in farenheit and kelvin

input_temp = int(input("Enter the teperature in celsius: "))

farenheit = (input_temp * 9/5) + 32
kelvin = input_temp + 273.15

print(f"Temperature in farenheit: {farenheit} F")
print(f"Temperatue in kelvin: {kelvin} K")