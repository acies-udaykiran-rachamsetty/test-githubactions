from src.sum import division
import unittest
from unittest.mock import patch
from src.customexception import RandomException


class Test(unittest.TestCase):

    def test_division(self):
        assert division(5, 3) == 1

    def test_division_exception(self):
        with self.assertRaises(RandomException) as context:
            division(5, 0)
        print(context.exception)
        # self.assertEqual(str(context.exception.message), "b should not be zero")


if __name__ == '__main__':
    unittest.main()
