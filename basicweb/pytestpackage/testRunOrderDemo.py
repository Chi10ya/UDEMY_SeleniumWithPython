import pytest

@pytest.mark.run(order=2)
def test_conftestdemo1_methodA(oneTimeSetUp, setUp):
    print("Running test run demo 1 method A")

@pytest.mark.run(order=4)
def test_conftestdemo1_methodB(oneTimeSetUp, setUp):
    print("Running test run demo 1 method B")

@pytest.mark.run(order=1)
def test_conftestdemo1_methodC(oneTimeSetUp, setUp):
    print("Running test run demo 1 method C")

@pytest.mark.run(order=3)
def test_conftestdemo1_methodD(oneTimeSetUp, setUp):
    print("Running test run demo 1 method D")