import unittest
from unittest.mock import patch
from src.GuessingLocation import *

class TestGuessingLocation(unittest.TestCase):

    def test_validate_guess(self):
        # Test cases for validateGuess method
        self.assertTrue(GuessingLocation.validateGuess(5))
        self.assertFalse(GuessingLocation.validateGuess(-1))
        self.assertFalse(GuessingLocation.validateGuess(10))

    def test_is_winner(self):
        # Test cases for isWinner method
        player_hits = {"Total": 5}
        self.assertEqual(GuessingLocation.isWinner(player_hits, "Player 1"), "Player 1")
        player_hits = {"Total": 3}
        self.assertEqual(GuessingLocation.isWinner(player_hits, "Player 2"), "")

    def test_guess_location(self):
        # Setup
        oppositionGrid = [
            ["Empty", "Empty", "Empty"],
            ["Empty", "Battleship", "Empty"],
            ["Empty", "Empty", "Empty"]
        ]
        guessingGrid = [
            ["O", "O", "O"],
            ["O", "O", "O"],
            ["O", "O", "O"]
        ]
        playerHits = {"Carrier": 0, "Battleship": 0, "Cruiser": 0, "Submarine": 0, "Destroyer": 0, "Total": 0}
        username = "TestUser"

        # Mock input to simulate user entering '2' for both x and y coordinates (1-based index)
        with patch('builtins.input', side_effect=["2", "2"]):
            # Execute
            resultGrid = GuessingLocation.guessLocation(oppositionGrid, guessingGrid, playerHits, username)

        # Verify
        expectedGrid = [
            ["O", "O", "O"],
            ["O", "X", "O"],
            ["O", "O", "O"]
        ]
        self.assertEqual(resultGrid, expectedGrid)
        self.assertEqual(playerHits["Battleship"], 1)

if __name__ == '__main__':
    unittest.main()