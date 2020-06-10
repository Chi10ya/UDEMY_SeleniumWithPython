# ************** 48: Inheritance

# Parent Class (or) Base Class (or) Super Class

class ParentCar(object):

    def __init__(self):
        print("Called the init in parent class")

    def StartEngine(self):
        print("Parent Class : Started Engine")

    def StopEngine(selfs):
        print("Parent Class : Stopped Engine")

# Child Class (or) Derived Class

class ChildClassBMW(ParentCar):

    def __init__(self):
        ParentCar.__init__(self)
        print("Child Class : BMW instance is created")

    def CarEngineCC(self):
        print("Child Class : Car Engine CC is 212224")

p1= ParentCar()
p1.StartEngine()
p1.StopEngine()

c2= ChildClassBMW()
c2.StartEngine()
c2.CarEngineCC()
c2.StopEngine()




