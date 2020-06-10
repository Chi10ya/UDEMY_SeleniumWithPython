"""
Exceptions are errors
We should handle exceptions in our code to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.hrml
"""

# *************** 51 - Exception Demo


def exceptionHandlingSession():
    try:
        a=10
        b=20
        c=0
        d=(a+b)/0
        print(d)
    except ZeroDivisionError: # you can mention the exception name or simply you can write except
        print("Oops exception raised")


exceptionHandlingSession()

# ************* 52: Finally and Else block


def exceptionHandlingSession2():
    try:
        a=10
        b=20
        c=10 # Put the value as 0 incase of exception is required.
        d = (a + b) / c
        print(d)
    except ZeroDivisionError: # you can mention the exception name or simply you can write except
        print("Oops exception raised. I am in except block")
        # raise Exception is for to see the exception details (Stack trace)
        raise Exception("This is an exception")
    # Else block is, what to do incase if exception is raised.
    else:
        print("Due to no exception raised. Else block is executed")
    # This finally block always execute no matter the exception is there or not.
    # It is used for disconnecting the DB connection and reconnecting or resetting the values
    finally:
        print("I am always there to execute. I am Finally block")


exceptionHandlingSession2()