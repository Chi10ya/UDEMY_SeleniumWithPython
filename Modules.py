"""
For to get the available python builtin libraries
URL: https://docs.python.org/3/library
"""

# ************ 54: Built in module

import math     # math is one of the builtin module
from math import sqrt      # This is importing the specific function from the module math




class BuiltInModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(20))
        print(sqrt(40))


md= BuiltInModulesDemo()
md.builtin_modules()


# ************** 55 : Create your own modules

#from chi10yamodules import CarDetails    # This is importing the user defined module. Module created in chi10yamodules
# or
from chi10yamodules.CarDetails import carInfo

class UserDefinedModule():

    def car_details(self):
        make= "Peugeot"
        model= "3008"
        country= "Ireland"
        #CarDetails.carInfo(make, model, country)
        #or
        carInfo(make, model, country)


udm= UserDefinedModule()
udm.car_details()