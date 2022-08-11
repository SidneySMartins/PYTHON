Kelvin = float(input('Temperatura em Kelvin: '))
Celsius = (Kelvin - 273.15)
Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
print('Kelvin: {:.2f}Kº\nCelsius: {:.2f}Cº\nFahrenheit: {:.2f}Fº'.format(
    Kelvin, Celsius, Fahrenheit))
