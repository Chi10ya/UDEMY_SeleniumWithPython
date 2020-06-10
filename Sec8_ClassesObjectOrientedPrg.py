"""
8: Classes - Object Oriented Programming
    45: Understanding objects / classes
    46: Create your own object
    47: Create your own methods
    48: Inheritance
    49: Method Overriding
    50: Practice exercise with solution

"""
# 45: Understanding objects / classes

# 46: Create your own object


class myClass(object): # Inherting the inbuilt object class

    def __init__(self, make):  # __init__ method is used to initialize all the objects which are created to the specific class
        self.make = make
        print(self.make)

    def myName(self, name):
        print(name)

    def myCountry(self, countryName):
        print(countryName)

mc = myClass("Puegot")
mc.myName("Chaitanya Ambica Yashvir Dhiyanshi")
mc.myCountry("IRELAND")

# 47: Create your own methods

class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car : "+self.make)
        print("Model of the car : "+self.model)

c1 = Car('Puegot', '880')
print(c1.make)
print(c1.model)
print(Car.wheels)
print(c1.wheels)

# 48: Inheritance

class Cars(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class BMW(Cars):
    def __init__(self):
        Cars.__init__(self)
        print("You just create the BMW instance")

    def headsUpFeature(self):
        print("Having an headsp feature")

c2 = Cars()
c2.drive()
c2.stop()

b1 = BMW()
b1.drive()
b1.stop()
b1.headsUpFeature()


#     49: Method Overriding

class MyCars(object):
    print('$'*50)

    def __init__(self):
        print("You just created the car instance. It is MyCars class and in __init__")

    def start(self):
        print("Car started.... in MyCars class")

    def stop(self):
        print("Car stopped.... in MyCars class")


class BMW(MyCars):

    def __init__(self):
        print("You just create the BMW instance. It is BMW class and in __init__")
        MyCars.__init__(self)

    def headsUpFeature(self):
        print("Having an headsup feature.. in BMW class")

    def start(self):
        super().start()
        print("Hi..Chaitanya, Welcome.. Today you are driving BMW car. It is in BMW class")
        super().stop()

c2 = MyCars()
c2.start()
c2.stop()

b1 = BMW()
b1.start()
b1.stop()
b1.headsUpFeature()
b1.start()


#     50: Practice exercise with solution


#*************************************************
# My Practice of Classes & Objects


class empInfo(object):
    def set_emp_details(self, empno, ename):
        self.empNo = empno
        self.empName = ename

    def get_emp_details(self):
        return self.empNo, self.empName

objEmp = empInfo()
objEmp.set_emp_details(7224, "Chaitanya")
empNo, empName = objEmp.get_emp_details()
print("Employee Number : "+str(empNo))
print("Employee Name : "+empName)



