import unittest
from unittest.mock import patch
from src.LoadData import ReadCSVFile, PlayerLoad
from src.Player import *
from src.ReadCSVInterface import ReadCSVInterface


class StubReadCSVFile(ReadCSVInterface):

    def get_file_data(self, filename):

        if filename == "players.csv":
            return [
                ["userName", "firstName", "lastName", "password"],
                ["player1", "Paul", "Chuckle", "ToMe"],
                ["player2", "Barry", "Chuckle", "ToYou"]
            ]



class TestCustomerLoad(unittest.TestCase):

    @patch("src.LoadData.ReadCSVFile", return_value=StubReadCSVFile())
    def test_load_customers(self, mock_read_csv_interface):
        player_load = PlayerLoad()

        players = player_load.load_players()

        self.assertEqual(len(players), 3)

    @patch("src.LoadData.ReadCSVFile", return_value=StubReadCSVFile())
    def test_get_raw_data(self, mock_read_csv_interface):
        player_load = PlayerLoad()

        players = player_load.get_raw_player()

        self.assertEqual(players[0], ["userName", "firstName", "lastName", "password"])

    @patch("src.LoadData.ReadCSVFile", return_value=StubReadCSVFile())
    def test_format_customers(self, mock_read_csv_interface):
        player_load = PlayerLoad()

        formatted_player = player_load.format_players()
        self.assertEqual(formatted_player, "firstName lastName\nPaul Chuckle\nBarry Chuckle\n")

if __name__ == '__main__':
    unittest.main()