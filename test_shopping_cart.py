""""
A simple test suite to verify the stdout of shopping_cart.py
"""
import unittest
import io
from unittest.mock import patch

class TestShoppingCart(unittest.TestCase):
    """For end-testing shopping_cart.py"""
    def test_shopping_cart_01(self):
        """
        Executes shopping_cart.py script and asserts its printed output.
        """
        gold_stdout = (
            "Item: Item A - Price: $10.99\n"
            "Item: Item B - Price: $5.99\n"
            "Item: Item C - Price: $8.49\n"
            "Total price: 25.47\n"
        )
        code = None
        with open('shopping_cart.py', encoding='utf8') as file:
            code = file.read()

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            exec(code, globals(), locals()) # pylint: disable=exec-used
            stdout_str = mock_stdout.getvalue()
            self.assertEqual(stdout_str, gold_stdout)

if __name__ == '__main__':
    unittest.main()
