# *******  30 Working with Cpomparators

"""
==   Equality
!=   Mot Equal to
<    Less Than
>    Greater than
<=   Less than or equal to
>=   Greater than or equal to

"""

bool_one = 10==11
print(bool_one)
not_equal= 10!=11
print(not_equal)
less_than= 10<11
print(less_than)
greater_than= 10>11
print(greater_than)
less_than_equal= 10<=11
print(less_than_equal)
greater_than_equal= 10>=11
print(greater_than_equal)

# ******** 31 Understanding boolean operators, 32 Boolean Operators
"""
AND : True AND True = True , rest all are False
OR : False OR False = False, rest all are True
NOT : NOT True = False ; NOT False = True
"""
print("-------------")
op1 = (10==10) and (10<9) #== False
op2 = (10==10) and (10>9) #== True
op3 = (10==10) or (10>9) #== True
op4 = (10!=10) or (10<9) #== False
not_false = not(10==10) #== False
not_true= not(10>10) #== True

print(op1)
print(op2)
print(op3)
print(op4)
print(not_false)
print(not_true)

# 32 Boolean Operators
"""
order of boolean operators
1: Not
2: And
3: Or
"""

bool_output= True or not False and False
print(bool_output) #== True

bool_output_1= (10==10 or not 10>10) and 10>10
#  ( True or True ) ==> True and False == > False
print(bool_output_1) # == False

# ******** 33 Conditional Logic. If else conditions
if 100 > 10:
     print("Hundred is greater than 10")

value= "green"
if value == "green":
     print("Go")
elif value == "Orange":
     print("Read to Start / Stop")
else:
     print("Stop")

# ************* 34: While Loop Demo
lp= 1
while(lp <= 10):
     print(f"Loop #  : {lp}")
     lp=lp+1

# Adding values to the list by using while loop

emptyList=[]
num= 0
while num<10:
     emptyList.append(num)
     num += 1
print(emptyList)

# Break Continue and While / Else
# Break
lp= 1
while lp <= 10:
     print(f"Loop #  : {lp}")
     lp=lp+1

     if lp == 8:
          print("Oops.. Restricted at 8")
          break
     print("Printing next value")

print("-*-"*20)

# Continue
lp= 1
while lp <= 10:
     print(f"Loop #  : {lp}")
     lp= lp+1
     if lp == 7:
          continue
     print("Wow.. Trigger initiated to Start")
     print("Printing next value")

# While Else
print("^V^"*20)
lp=20
while lp <= 10:
     print(f"Loop #  : {lp}")
     lp=lp+1

     if lp == 8:
          print("Oops.. Restricted at 8")
          break
     print("Printing next value")
else:
     print("While condition is not satisfied")

# 36: For Loop Demo
"""
Executable statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""

myName = "Chaitanya"
for c in myName:
     if c == 'a':
          print('A', end=' ')
     else:
          print(c, end=' ')

myCars= ['BMW', 'BENZ', "AUDI", 'VOLVO']
for myCar in myCars:
     print(myCar, end=' ')

nums= [1, 2, 3, 4]
for n in nums:
     print(n*10)

# Accessing dictionary key and value by using for
dic= {'one':1, 'two':2, 'three':3}
for k in dic:
     print(k+" "+str(dic[k]))

for k, v in dic.items():
     print("Key :"+k)
     print("Value :"+str(v))

# 37: Iterating multiple lists : Using the zip function

l1= [8, 2, 3]
l2= [6, 7, 8, 9, 10]

for a, b in zip(l1, l2):
     if a > b:
          print(a)
     else:
          print(b)

# 38: Using range function in For Loop
"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""
print(" $ "*20)
for i in range(12, 23):
     print(i)

print(" ")
print(list(range(1, 22)))
print(" ")
a = range(0, 24, 2)
print(a)
print(list(a))

lis= [2, 4, 6, 8]
for num in range(1, 9):
     print(num)
















