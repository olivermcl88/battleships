import unittest
from unittest.mock import patch, MagicMock

from src.Player import Player
from src.LogIn import LogIn
from src.LoadData import PlayerLoad



class TestLogIn(unittest.TestCase):

    def test_get_password(self):
            logIin = LogIn()
            self.assertEqual("ToMe", logIin.get_password("player1"))
            self.assertEqual("ToYou", logIin.get_password("player2"))

    def test_login_success(self):
        login_instance = LogIn()

        login_instance.log_in_function = MagicMock(return_value=1)
        # 'x' tests the input validation followed by the valid input of 'Y'
        with patch('builtins.input', side_effect=['x', 'Y']) as _input:
            self.assertEqual(1, login_instance.log_in())

        login_instance.log_in_function = MagicMock(return_value=0)
        with patch('builtins.input', return_value='Y') as _input:
            self.assertEqual(0, login_instance.log_in())

    def test_log_in_function(self):
        login_instance = LogIn()

        #Tests when the correct password is entered
        login_instance.get_password = MagicMock(return_value="4567")
        with patch('builtins.input', side_effect=['sean@email.co.uk', '4567']) as _input:
            self.assertEqual(1, login_instance.log_in_function())

        #Tests when the incorrect password is entered
        with patch('builtins.input', side_effect=['sean@email.co.uk', '1520']) as _input:
            self.assertEqual(0, login_instance.log_in_function())

        #Tests when username is not valid
        login_instance.get_password = MagicMock(return_value="")
        with patch('builtins.input', return_value='sean@email.co.uk') as _input:
            self.assertEqual(0, login_instance.log_in_function())


if __name__ == '__main__':
    unittest.main()


