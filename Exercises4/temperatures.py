conversion_c = 273.15

my_kelvin = [175, 189, 210, 225, 236, 245, 259, 310, 330, 350]
my_celcius = [(round(kelvin - conversion_c, 2)) for kelvin in my_kelvin] 
print(my_celcius)
my_fahrenheit = [(round(fahren * 1.8 + 32, 2)) for fahren in my_celcius] 
print(my_fahrenheit)
