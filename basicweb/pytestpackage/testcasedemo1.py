import pytest
"""
When using pytest, it is very important to follow naming conventions.

If we don't follow naming conventions, then pytest will not pick up tests from the file.

File names should start or end with “test”, as in test_example.py or example_test.py
Class name should start with “Test”, as in TestExample
Test method names should start with “test_”, as in test_example
You can refer to the official documentation for more details:

http://pytest.readthedocs.io/en/reorganize-docs/new-docs/user/naming_conventions.html
"""

@pytest.fixture() # Decorator -->  fixture will be executed only once before every method and after every method.
def setUp():
    print("Once before every method")

def test_methodA(setUp):
    print("Running method A")

def test_methodB(setUp):
    print("Running method B")

# Command for to execute the code in terminal
# ===> Go to you package location and enter the command as py.test -v -s
# ===> or enter the command as py.test -s testcasedemo2 // For to run a specific file.