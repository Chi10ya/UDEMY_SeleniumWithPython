import pytest


@pytest.yield_fixture() # Decorator ---> yield.fixture will be executed once after before every method and after every method.
def setUp():
    print("Once before every method")
    yield
    print("Once after every method")


@pytest.yield_fixture(scope="module") # Decorator ---> yield.fixture with scope = "module" means it will be executed once after before every module / file and after every module / file
def oneTimeSetUp():
    print("Start : --> Once before every module / file")
    yield
    print("End : --> Once after every module / file")