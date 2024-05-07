import unittest
from unittest.mock import patch

from src.ReadCSVFile import ReadCSVFile
from src.SignUp import SignUp


class SignUpTest(unittest.TestCase):
    def test_get_password(self):
        sign_up = SignUp()
        self.assertEqual("ToMe", sign_up.get_password("player1"))
        self.assertEqual("ToYou", sign_up.get_password("player2"))

    def test_sign_up(self):
        sign_up = SignUp()

        with patch('builtins.input', return_value='admin@email.com'):
            self.assertIsNone(sign_up.sign_up())


if __name__ == '__main__':
    unittest.main()
