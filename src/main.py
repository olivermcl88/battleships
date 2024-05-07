from typing import Self
from Setup import Setup
from GuessingLocation import GuessingLocation 
from LogIn import *
from SignUp import *
from WinnersReward import *
from LoadData import *

class Main:
    def main():
        Player1 = LogIn()
        login_facility(Player1)
        Player1Username = LogIn.get_username(Player1)

        Player2 = LogIn()
        login_facility(Player2)
        Player2Username = LogIn.get_username(Player2)

        player1Grid = Setup.pickBoatPosition(Player1Username)
        player2Grid = Setup.pickBoatPosition(Player2Username)

        winner = GuessingLocation.main(player1Grid,player2Grid,Player1Username,Player2Username)

        if winner == "Player 1":
            print(f"\n{Player1Username} wins")
        else:
            print(f"\n{Player2Username} wins")

def login_facility(log_in):
    loggedIn = 0
    while loggedIn == 0:
        loggedIn = log_in.log_in()
        if loggedIn == 1:
            break 
        else:
            print("Incorrect details, please try again.")   
        


if __name__ == '__main__':
    Main.main()

