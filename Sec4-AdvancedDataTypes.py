"""
4: Advanced data types
    24: List and accessing the elements
    25: List Methods
    26: Working with Dictionary
    27: Nested dictionary.
    28: Dictionary Methods
    29: Working with Tuple

Data type to store more than one value in one variable name
List items as in square brackets, separated with "," [1, 2, 3]
Dictionary items are in curly brackets {} in key:value pairs, separated with "," ==> like ==> {'k1':'v1', 'k2':'v2'}. Dictionary is mutable.
Tuple items are in brackets. It is almost like a list but they are imutable. It means you cannot change them
"""

# 24: List and accessing the elements

cars = ["bmw", "honda", "audi"]
print(cars)
for car in cars:
    print(car)

print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0]+num_list[1]
print(sum_num)

cars[1] = "Puegot"
print(cars)

vehicles = []
vehicles.append("Volvo Bus")
vehicles.append("Benz Bus")
print(vehicles)

# 25: List Methods
print(len(cars))
length = len(vehicles)
print(length)

cars.append("Volvo")
print(cars)

cars.insert(2, "jeep")
print(cars)

print(cars.index("Puegot"))

popCars = cars.pop()
print(cars)

cars.remove("jeep")
print(cars)

slicingCars = cars[1:]
print(slicingCars)
slicingCars = cars[:-1]
print(slicingCars)
cars.sort()
print(cars)

# 26: Working with Dictionary

car = {'make':'bmw', 'model':'550c', 'year': '2016'}
print(car)
print(car['make'])

d={}
d['One'] = 1
d['Two'] = 2
d['Three'] = 3
d['Four'] = 4
d['Five'] = 4
print(d)

sum_1 = d['Two'] + 8
print(sum_1)
d['Five'] = d['Two'] + 8 + d['One'] + d['Four']
print(d['Five'])

# 27: Nested Dictionary

myCars = {'bmw': {
                    'model' : '550i',
                    'year' : '2019'
                 },
          'benz': {
                    'model': 'E350',
                    'year': '2020'
                  }
         }
print(myCars)
print(myCars['bmw']['year'])
print(myCars['benz']['model'])

# 28: Dictionary Methods
print('^'*50)
print(myCars.keys())
print(myCars.values())
print(myCars.items())

print("Our Family Cars")
ammuCars = myCars.copy()
print(ammuCars)
print(myCars)

#29: Working with Tuple

myTupple = (2, 2, 21, 24)
print(myTupple)
print(myTupple[1])
print(myTupple[1:])
print(myTupple.index(2))
print(myTupple.count(2))








