from src.sum import sum
import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        assert sum(5,6) == 11
        assert sum(-1,6) == 5
        assert sum(-1,-1) == -2
