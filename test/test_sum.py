from src.sum import division
import unittest
from unittest.mock import patch


class Test(unittest.TestCase):

    def test_division(self):
        assert division(5, 3) == 1

    def test_division_exception(self):
        with patch('src.sum.exception') as mock_exception:
            mock_exception.side_effect = ZeroDivisionError("Division by zero is not allowed")

            with self.assertRaises(ZeroDivisionError) as context:
                division(5, 0)

            self.assertEqual(str(context.exception), "Division by zero is not allowed")


if __name__ == '__main__':
    unittest.main()
