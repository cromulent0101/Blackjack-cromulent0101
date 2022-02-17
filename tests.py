import unittest
from cardutils import getHandValue

class TestStringMethods(unittest.TestCase):

    def test_many_aces(self):
        self.assertEqual(getHandValue([1,1,1,1,1,1,1,1,1,10])[0],19)

    def test_two_aces(self):
        self.assertEqual(getHandValue([1,1])[0],12)

    def test_soft_hard_17(self):
        self.assertEqual(getHandValue([1,6])[1],True)
        self.assertEqual(getHandValue([10,7])[1],False)
        self.assertEqual(getHandValue([1,1,1,1,1,2])[1],True)

    def test_alternating_aces(self):
        self.assertEqual(getHandValue([1,6])[0],17)
        self.assertEqual(getHandValue([1,6,1])[0],18)
        self.assertEqual(getHandValue([1,6,1,4])[0],12)

    def test_crazy_blackjack(self):
        self.assertEqual(getHandValue([2,2,2,2,2,2,2,2,2,2,1])[0],21)


if __name__ == '__main__':
    unittest.main()