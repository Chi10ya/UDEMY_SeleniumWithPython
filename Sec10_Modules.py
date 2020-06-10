"""
Section 10: Modules
    54: BuiltIn Modules
    55: Create your own modules
"""

#: 54: BuiltIn Modules

#import math
from math import sqrt


class ModeulesDemo():
    def builtin_modules(self):
        try:
            print(sqrt(2))
        except:
            print("Opps Exception raised")
        else:
            print("There is no exception and sqrt function performed well")


m1 = ModeulesDemo()
m1.builtin_modules()

# 55: Create your own modules

from chi10yamodules import CarDetails

def car_description():
       make = "PUEGOT"
       model =  "880"
       country = "Ireland"
       CarDetails.carInfo(make, model, country)


car_description()







