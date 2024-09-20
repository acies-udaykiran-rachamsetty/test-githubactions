from src.sum import getLucky
import unittest


class Test(unittest.TestCase):

    def test_getLucky(self):
        assert getLucky("iiii", 1) == 36

    def test_getLucky_1(self):
        assert getLucky("leetcode", 2) == 6


if __name__ == '__main__':
    unittest.main()
