import unittest
from game import getHandValue

class TestStringMethods(unittest.TestCase):

    def test_many_aces(self):
        self.assertEqual(getHandValue([1,1,1,1,1,1,1,1,1,10])[0],19)

    def test_two_aces(self):
        self.assertEqual(getHandValue([1,1])[0],12)

    def test_soft_hard_17(self):
        self.assertEqual(getHandValue([1,6])[1],True)
        self.assertEqual(getHandValue([10,7])[1],False)
        self.assertEqual(getHandValue([1,1,1,1,1,2])[1],True)

if __name__ == '__main__':
    unittest.main()