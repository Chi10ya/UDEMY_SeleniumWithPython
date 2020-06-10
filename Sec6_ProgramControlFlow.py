"""
6: Program Control Flow
    33: Conditional Logic - If Else conditions
    34: While lopp Demo
    35: Break Countinue and While / Else
    36: For Lopp demo
    37: Iterating multiple list - Using the Zip function
    38: Using range function in For Loop
"""
# 33: Conditional Logic - If Else conditions

if 100 < 10:
    print("Hundred is greater than 10")
elif (100 == 100):
    print("Hundred is equal to Hundred")

age = 14
if age <=18:
    print("Driving license is not allowed")
else:
    print("Driving license is allowed")

# 34: While lopp Demo

x=0
while x < 10:
    print("Value of x is :"+str(x))
    x=x+1

l=[]
num = 0
while num <10:
    l.append(num)
    num += 1

print(l)

# 35: Break Continue and While / Else
# Break : To break out of the closest enclosing loop
# Continue : Go to the start of the closest enclosing loop

# Break
print('-_'*40)
print("Break")
x=0
while x < 10:
    print("Value of x is : "+str(x))
    x = x+1

    if x == 8:
        break
    print("This example is awesome")
print("Just broke out of the loop")


# Continue
print('-_'*40)
print("Continue")
x=0
while x < 10:
    print("Value of x is : "+str(x))
    x = x+1

    if x == 8:
        continue
    print("This example is awesome")
    print("**")
print("Just broke out of the loop")

# While - Else

print('-_'*40)
print("Else")
x=20
while x < 10:
    print("Value of x is : "+str(x))
    x = x+1
    print("This example is awesome")
else:
    print("Just broke out of the loop")

#   36: For Loop demo
"""
Execute statement repeatedly. Conditions are used to stop the excution of loops.
Iterable items are String, List, Tuple, Dictionary
"""

myFamily = "ChaitanyaAmbicaYashvirDhiyanshi"

for c in myFamily:
    if c == 'a':
        print('A', end='')
    else:
        print(c, end='')
print()

cars = ['bmw', 'benz', 'honda']
for car in cars:
    print(car, end=' ')
print()

nums = [1, 2, 3]
for n in nums:
    print(n*10, end=' ')
print()

print("Dictionary")
dic = {'one':1, 'two':2, 'three':3}
for k in dic:
    print(k+" "+str(dic[k]))

for k, v in dic.items():
    print("Keys : "+k)
    print("Values : "+str(v))


#    37: Iterating multiple list - Using the Zip function
l1 = [1, 2, 3]
l2 = [6, 7, 8, 9,]

for a, b in zip(l1, l2):
    print(str(a)+' '+str(b))


#   38: Using range function in For Loop
""" Built-in function . Creates a sequence of numbers but does not save them in memory
    Verify useful for generating numbers
"""
print(list(range(0, 10)))
a = range(10, 20, 2)
print(a)
print(type(a))
print(list(a))