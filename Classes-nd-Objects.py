"""
Object Oriented Programming
"""
# ******* 45: Understanding Objects / Classes

s="Chaitanya Ambica Yashvir Dhiyanshi"
# Here s is an object and upper and lower are the builtin methods.
print(len(s))
print(s.upper())
print(s.lower())

# ******* 46: Create your own object

class MyCars(object):

    def __init__(self, make, model='2020'):
        self.make= make
        self.model= model

mc= MyCars("BMW")
print("My Car Make is :"+ mc.make)
print("My Car Model is :"+ mc.model)

# ******* 47: Create your own methods

class MyOwnCars(object):

    wheels = 5   # member variables

    def __init__(self, make, model, cost):

        # Instance Variables
        self.make= make
        self.model= model
        self.cost= cost

    def display_my_cars(self):
        print("Make of the car is :"+self.make)
        print("Model of the car is : "+self.model)
        print(f"Cost of the car is  {self.cost}")

    print(f"Car is having wheels {wheels}")


c2= MyOwnCars("BENZ", '2020', 350000)
c2.display_my_cars()
c2.wheels = 4
print(f" Printing the wheels after changing the member variable value {c2.wheels}")
print(f" Calling the member variable value by using Class name {MyOwnCars.wheels}")


# ************ My Own Practice
class Employee(object):

    def __init__(self, empNo, eName):
        self.empNo = empNo
        self.eName = eName

    def displayempnames(self):
        print(f"Employee Number {self.empNo}")
        print(f"Employee Name {self.eName}")


emp = Employee(212224, 'Chaitanya')
emp.displayempnames()

