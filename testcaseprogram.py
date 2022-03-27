import unittest

import Programs

class Armstrong_test(unittest.TestCase):

    def setUp(self):
        self.a = 407

    def tearDown(self):
        self.a = 0

    def test_Armstrong(self):
        c = Programs.Armstrong_number(self.a)
        self.assertTrue(c)

class divisible_test(unittest.TestCase):

    def setUp(self):
        self.b = 50

    def tearDown(self):
        self.b = 0

    def test_divisibleby5(self):
        c = Programs.divisible_by_5(self.b)
        self.assertTrue(c)

class largest_test(unittest.TestCase):

    def setUp(self):
        self.a = 1000
        self.b = 525
        self.c = 960

    def tearDown(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def test_largest(self):
        c = Programs.largest_number(self.a,self.b,self.c)
        self.assertEqual(self.a,c)

class EvenorOdd_test(unittest.TestCase):

    def setUp(self):
        self.a = 151
        self.b = 100

    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_evenorodd1(self):
        c = Programs.check_Even_or_Odd(self.a)
        self.assertFalse(c)

    def test_evenorodd2(self):
        c = Programs.check_Even_or_Odd(self.b)
        self.assertTrue(c)

if __name__ == "__main__":
    unittest.main()