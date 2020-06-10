import pytest

"""
file name should start with test
test method name should start with test

py.test -v -s testcasedemo2.py # run tests in module/file
py.test -v -s <path of the directory / package> # run all the tests in that particular module / package
py.text -v -s testcasedemo2.py::test_methodA # runs the specific method in a specific module / file.

-s to print statements
-v verbose
"""

@pytest.yield_fixture() # Decorator ---> yield.fixture will be executed once after before every method and after every method.
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")


# Command for to execute the code in terminal
# ===> Go to you package location and enter the command as py.test -v -s
# ===> or enter the command as py.test -s testcasedemo2 // For to run a specific file.