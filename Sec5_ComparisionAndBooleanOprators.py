"""5: Comparision And Boolean Operators
    30: Working with Comparators
    31: Understanding Boolean Operators
    32: Boolean Operators - Order of Precedence

= = --> Value Equality
!= --> Not Equal To
< --> Less than
> --> Greater than
<= --> Less than or equal to
>= --> Greater than or equal to

"""
# 30: Working with Comparators

bool_one = 10 == 10
not_equal = 10 != 11
less_than = 10 < 10
greater_than = 10 > 10
lt_equal = 9<=10
gt_equal = 10>=12

print(bool_one)
print(not_equal)
print(less_than)
print(greater_than)
print(lt_equal)
print(gt_equal)

if(bool_one): # By default it returns true
    print("It is true") #
else:
    print("It is false")


# 31: Understanding Boolean Operators

# AND : True AND True = True, rest all are False
# OR : False OR False = False, rest all are True
# NOT : Not True = False ; Not False = True
print("****************AND****************")
and_output1 = (10 == 10) and (10 > 9)
print(and_output1)
and_output2 = (10 == 10) and (10 < 9)
print(and_output2)
and_output3 = (10 > 10) and (10 < 9)
print(and_output3)
print("****************OR****************")
or_output1 = (10 == 10) or (10 > 9)
print(or_output1)
or_output2 = (10 == 10) or (10 < 9)
print(or_output2)
or_output3 = (10 > 10) or (10 < 9)
print(or_output3)
print("****************NOT**************")
not_true = not(10 == 10)
print(not_true)
not_false = not(10 >= 20)
print(not_false)


# 32: Boolean operators - Order of precedence

bool_output = True or not False and False  # ==> False


