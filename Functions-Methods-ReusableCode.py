# 39: Understanding methods

# Method without arguments
def sum_num():
     print(3+2)

sum_num()


# Method with arguments
def sum_nums(n1, n2):
     print(n1+n2)

sum_nums(4, 4)

# ******************** 40: Working with Return Values

def sumTwoNumbers(n1, n2):
     sumVal= n1+n2
     return sumVal

sumResult= sumTwoNumbers(20, 10)
print(sumResult)


def isMetro(city):
     l=['sfo', 'nyc', 'la']

     if city in l:
          return True
     else:
          return False

x= isMetro('sfo')
if x == True:
     print("Yes, it is a metro")
else:
     print("No, it is not a metro")

#41 ***********************  Working with Positional / Optional Parameters
"""
Positional Parameters
They are like optional parameters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums(n2, n1):
     print(n1+n2)


sum_nums(n1=8, n2=11)


def sum_nums2(n1, n2=4):
     print("Method formal parameters having the default value")
     print(n1+n2)


sum_nums2(40, n2=12)

# **************** 42: Understanding variable scope * === Using Global

a= 10
def test_method(a):
     print("Value of local is : "+str(a))
     a=2
     print("New Value of local a is : "+str(a))

print("Value of global a is : "+str(a))
test_method(a)
print("Did the value of global a change ? : "+str(a))

# by using global keyword for to access global value inside the method

a= 10 # global variable with value as 10

def test_methods():
     global a
     print("Value of 'a' inside the method is : "+str(a))
     a=2
     print("New Value of 'a' inside the method is changed to : "+str(a))


print("Value of global a is : "+str(a))
test_methods()
print("Did the value of global a change ? : "+str(a))

# ******************* 43: More built in Functions
"""
Some built in functions
max(), min(), abs(), type()
"""

def largestVal(*args): # *args is letting to accept multiple arguments
     print(max(args))
     print(min(args))

def abs_function(a):
     print(abs(a))

largestVal(10, 20, 30, 40, -1, -10, -15)
abs_function(-15)

print(type(99))
print(type(-10))
print(type('Chaitan'))








