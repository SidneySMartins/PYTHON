Fahrenheit = float(input('Temperatura em Fahrenheit: '))
Celsius = (Fahrenheit - 32)*5/9
Kelvin = (Celsius + 273.15)
print('Fahrenheit: {:.2f}Fº\nCelsius: {:.2f}Cº\nKelvin: {:.2f}Fº'.format(
    Fahrenheit, Celsius, Kelvin))
