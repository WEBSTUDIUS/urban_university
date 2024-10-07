import unittest2

def calc_add(a, b):
    return a + b

class CalcTest(unittest2.TestCase):
    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(calc_add(1, 2), 3)
