import unittest

class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
         print("*#"*30)
         print("I will run only once before all tests")
         print("*#"*30)

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a, "a is not true")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Test"
        b = "Test"
        self.assertEqual(a, b, msg="'a' is not equal to 'b'")

    def tearDown(self):
        print("I'll run after every test")

    @classmethod
    def tearDownClass(cls):
        print("*#"*30)
        print("I will run only once after all tests")


if __name__ == '__main__':
    unittest.main(verbosity=2)