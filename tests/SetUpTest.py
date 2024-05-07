import unittest
from src.Setup import Setup

class TestSetup(unittest.TestCase):

    def test_validateCoOrdinate(self):
        self.assertTrue(Setup.validateCoOrdinate(5))
        self.assertFalse(Setup.validateCoOrdinate(-1))
        self.assertFalse(Setup.validateCoOrdinate(9))

    def test_isShipAlreadyThere(self):
        grid = [["Empty"] * 9 for _ in range(9)]
        self.assertTrue(Setup.isShipAlreadyThere(0, 0, 0, 4, grid, 5))
        grid[0][0] = "Carrier"
        self.assertFalse(Setup.isShipAlreadyThere(0, 0, 0, 4, grid, 5))

    def test_placeBoat(self):
        grid = [["Empty"] * 9 for _ in range(9)]
        Setup.placeBoat("Destroyer", 2, 0, 0, 1, grid)
        self.assertEqual(grid[0][0], "Destroyer")
        self.assertEqual(grid[0][1], "Destroyer")

if __name__ == '__main__':
    unittest.main()