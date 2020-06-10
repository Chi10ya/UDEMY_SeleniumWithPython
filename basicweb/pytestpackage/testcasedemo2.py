import pytest

"""
After pytest version 2.10, you do not need @pytest.yield_fixture explicitly to use yield.
The default @pytest.fixture also supports yield.
It means the code will work if you are using @pytest.yield_fixture or @pytest.fixture.
This screenshot is from pytest website:
http://doc.pytest.org/en/latest/fixture.html
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