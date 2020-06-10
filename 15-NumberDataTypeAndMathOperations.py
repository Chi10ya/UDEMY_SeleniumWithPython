int_num= 10
float_num= 212224.07

print(int_num)
print(float_num)

print(type(int_num))
print(type(float_num))

a=10
b=20

add= a+b
print(add)

sub= b-a
print(sub)

multi=a*b
print(multi)

div=b/a
print(div)

# ************* 16: Numbers -Exponentiation and Modulo
# Exponentiation

exponents= 10 ** 20
print(exponents)

"""
     This is a multiline comment
"""
# Modulo - It reurns the remainder
remainder= 10 % 3
print(remainder)

# ************** 17: Arithmetic order of precedence

# Boolean Data Type

a= True
b= False
print(a)
print(b)
print(bool(0))
print(bool(1))
print(bool(2))

c=""
print(bool(c))

# ******************* 19: Working with strings
"""
Examples to show how strings works in python

Sequence of characters
Contains a-z, 0-9, @
In double or singel quotes

"""

a= "This is a simple string"
b= 'Using single quotes'
c= 'Need to use double "quotes" inside a sting'
d= "Need to use single 'quotes' inside a sting"
e= "Typing this message\
in two lines"
print(a)
print(b)
print(c)
print(e)

# ******************** 20: String Methods - Part 1

"""
Examples to show available string methods in python
"""
# Accessing characters in a string
first= "Chaitanya"[0]
print(first)
print(first.lower())
print(first.upper())
print(len(first))
print(first + str(212224))

# Concatenation
print("Hello"+" "+"World !!!")


# ******************** 21: String Methods - Part 2
# Replace
a= "1abc2abc3abc4abc"
print(a.replace('abc', 'ABC '))

# Substring
sub= a[1]
print(sub)
print("------------")
sub= a[1:len(a)]
print(sub)
print("************")
print(a[1:len(a):2])


# ******************* 22: More String slicing and Indexing

print("###########")
print(a[1:])
print(a[:len(a)])
print(a[-1])
print(a[:-2])
print(a[::2])
print(a[::-1])

# ****************** 23: Strings Formating
city= "Cork"
event= "Movie stars gathering"

print("Welcome to "+city+" and enjoy the event "+event)
print("Welcome to %s and enjoy the event %s" %(city, event))
print("Welcome to {} and enjoy the event {}" .format(city, event))
print(f"Welcome to {city} and enjoy the event {event}")

abc = "one two three"
l=abc.split()
print(l)

a="test"

# ****************** 24: [] List and accessing the elements & 25: List Methods
# 24:
"""
Data type to store more than one value in one variable name
List items are in square brackets [], separated with "," [1,2,3]
Index starts with 0 
List is Mutable
"""
cars = ["BMW", "AUDI", "BENZ"]
print(cars)
print(cars[0])
joinCars = cars[0]+" "+cars[1]+" "+cars[2]
print(joinCars)
for i in cars:
     print(f"Car Name : {i}")

cars[2]= "VOLVO"
print(cars)

# 25: List Methods

length = len(cars)
print(length)

cars.append("BENZ")
print(cars)

cars.insert(-1, "Audi")

cars.insert(1, "Puegot")
print(cars)

ind= cars.index("AUDI")
print(ind)

y=cars.pop()
print(y)

cars.remove("Audi")
print(cars)

slicing= cars[0:2]
a= cars[1:]
print(slicing)
print(a)
print("_-_-_-")
cars.sort()
print(cars)
print("........")
print(cars.count("Audi"))

# ************************* 26 : {} Working with Dictionary , 27: Nested Dictionary, 28: Dictionary Methods
# 26 : Working with Dictionary
"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets {} in key:value pairs, separated with "," {'k1':'v1', 'k2':'v2'}
Not sequenced, no indexing -> Nothing
Dictionary is Mutable
"""

junkChar= {'k1':'v1', 'k2':'v2'}
emptyDict={}

print(junkChar)
print(junkChar['k1'])

k1val= junkChar['k1']
print(k1val)

emptyDict['one']= 1
emptyDict['two']= 2

print(emptyDict)
sumDict = emptyDict['two'] + 212222
print(sumDict)

#27: Nested Dictionary

cars = {
     'bmw':
          {'model':'550i', 'year':2019},
     'audi':
          {'model':'212224', 'year':2019}
}
print(cars)
bmwYear= cars['bmw']['year']
print(bmwYear)
audiModel= cars['audi']['model']
print(audiModel)

print("<><><><><><>")
d={"k1":
        [1,2,3],
   "k2":
        [4,5,6]
   }
e= d["k1"][2]
print(e)
print("<><><><><><>")

# 28: Dictionary Methods

print(cars.keys())
print(cars.values())
print(cars.items())
carsCopy = cars.copy()
print(carsCopy)


# ************************* 29 : () Working with Tuple.
"""
Tuple is Immutable
It is like a list but they are immutable
It means you can't change them
Tuple is with round brackets ()
Only two methods available in Tuple. Those are Count and Index
"""

my_tuple = (1, 2, 3, 3, 3, 3, 3, 2, 4)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1:])
print(my_tuple.index(2))
print(my_tuple.count(3)) # It counts particular item in tuple.
