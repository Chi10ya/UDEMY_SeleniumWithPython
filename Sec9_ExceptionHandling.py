"""
Section 9: Exception Handling ---> try, except, raise, else, finally
    51: Exception Handling Demo
    52: Finally and Else
    53: Practice Exercise with solution *** Homework

Exceptions are errors

We should handle exceptions in our code to make sure the code is working the way we want and is handling all the
unwanted issues link to 3.5 built-in exception - https://docs.python.org/3/library/exceptions.html
"""

# 51: Exception Handling Demo
# 52: Finally and Else

def exceptionHandling():
    try:
        a = 20
        b = 10
        c = 5

        d = (a+b)/c
        print(d)
    except ZeroDivisionError:
        print("In the except block, this is not possible - Zero Division Error. I am raised because there is an exception")
        raise Exception ("This is an exception raised at exceptionHandling method")
    except TypeError:
        print("In the except block, can't add string to integer. I am raised because there is an exception")
    else:
        print("This block is executed because there is no Exception")
        d = d*222124
        print(d)
    finally:
        print("Finally, this block finally always executed. I always execute whether there is an exception or not")


exceptionHandling()


# 53: Practice Exercise with solution *** Homework

def dictCar(element):
    print("--> "+element)
    try:
        dictCar = {"make":"bmw", "model":"2020", "year":"2020"}
        print(dictCar[element])
    except:
        print("Key not found")
    else:
        print("Wow the element is found")


dictCar('make')


