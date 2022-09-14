""" importing an entire module and use dot notation"""
import p179_car 

from p179_car import ElectricCar
from p179_car import Car


my_beetle = p179_car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = p179_car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

""" or import each module by separate and call it 
without using dot notation """

my_beetle2 = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla2 = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())