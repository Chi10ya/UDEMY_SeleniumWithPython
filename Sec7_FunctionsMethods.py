"""
7: Functions / Methods - Working with Reusable code
    39: Understanding Methods
    40: Working with Return values
    41: Working with Positional / Optional Parameters
    42: Understanding variable scope
    43: More built-in functions.
    44: Practice Exercise with solution *** Homework
"""
# 39: Understanding Methods

def cal(a, b):
    sumTot=a+b
    mulTot=a*b
    subTot=b-a
    return sumTot, mulTot, subTot


sumTot, mulTot, subTot = cal(5, 5)
print(sumTot)
print(mulTot)
print(subTot)

def printHi():
    i=1
    while i<=10:
        print("Hi "+str(i))
        i+=1

printHi()

# 40: Working with Return values

def isMetro(city):
    l=['sfo', 'irl', 'can']
    if city in l:
        return True
    else:
        return False


x= isMetro('irl')
print(x)

# 41: Working with Positional / Optional Parameters
"""
They are like optional parameters
And can be assigned a default value, if no value is provided from outside.
"""

def sum_nums(n1, n2=5):
    return n1+n2


sum1 = sum_nums(10)
print(sum1)

sum2 = sum_nums(n2=10, n1=22)
print(sum2)

# 42: Understanding variable scope

a = 10      # It is having a gloabl scope
def test_method(a):
    print("Value of local a is :"+str(a))
    a=2     # It is having a local scope
    print("New Value of local a is :"+str(a))


print("Value of global a is :"+str(a))
test_method(a)
print("Did the value of global a change ?"+str(a))

# By using global keyword for to access the global variable inside the method.

aa = 30      # It is having a gloabl scope
def test_method1():
    global aa
    print("Value of 'a' inside the method is  :"+str(aa))
    aa=2     # It is having a local scope
    print("New Value of 'a' inside the method is changed to:"+str(aa))


print("Value of global a is :"+str(aa))
test_method1()
print("Did the value of global a change ?"+str(aa))

# 43: More built-in functions.

def largest_num(*args): # Here * means it accepts as N number of arguments
    print("Printing Min and Max value")
    return min(args), max(args)


minVal, maxVal = largest_num(10, 22, 3, 44, -20, -10)
print(maxVal)
print(minVal)


#     44: Practice Exercise with solution *** Homework







