class GuessingLocation():
    
    def isWinner(playerHits, turn):
        if playerHits["Total"] == 5:
            return turn
        else:
            return ""

    def validateGuess(guess):
        if guess >= 0 and guess <=9:
            return True
        else:
            return False
        
    def displayGrid(grid):
        # Print column headers with adjusted spacing to align with the grid
        for i in range(len(grid)):
            column_headers = " "* 1 + str(i+1)  + " "* 1
            print(column_headers, end=" ")

        # Separator line
        print("\n   " + "-" * (len(grid[0]) * 4 ))

        # Print each row with row index
        for index, row in enumerate(grid):
            row_str = f"{index+ 1} | " + " | ".join(row)
            print(row_str)
            print("   " + "-" * (len(row_str) - 1))
    
    def guessLocation(oppositionGrid, guessingGrid, playerHits,username ):
        shipLength = {"Carrier" : 5, "Battleship": 4, "Cruiser" : 3, "Submarine" : 3, "Destroyer" : 2 }
        validGuess = False

        GuessingLocation.displayGrid(guessingGrid)

        while validGuess == False:
            xGuess = int(input(f"\n{username}, what is the x co ordinate of your guess: "))-1
            validX = GuessingLocation.validateGuess(xGuess)
            yGuess = int(input(f"\n{username}, what is your y co ordinate guess: "))-1
            validY = GuessingLocation.validateGuess(xGuess)
            print("\n")

            if validX == True and validY == True:
                validGuess = True
    
        if oppositionGrid[yGuess][xGuess] == "Empty":
            print("Miss")
            guessingGrid[yGuess][xGuess] = "E"
        else:
            guessingGrid[yGuess][xGuess] = "X"
            print("Hit")

            if oppositionGrid[yGuess][xGuess] == "Carrier":
                playerHits["Carrier"] += 1
            elif oppositionGrid[yGuess][xGuess] == "Battleship":
                playerHits["Battleship"] += 1
            elif oppositionGrid[yGuess][xGuess] == "Cruiser":
                playerHits["Cruiser"] += 1
            elif oppositionGrid[yGuess][xGuess] == "Submarine":
                playerHits["Submarine"] += 1
            else: 
                playerHits["Destroyer"] += 1

            for ship in shipLength:
                if playerHits[ship] == shipLength[ship]:
                    print(ship + " has been destroyed!")
                    playerHits[ship] += 1
                    playerHits["Total"] += 1
        return guessingGrid

            

    def main(player1Grid,player2Grid,Player1Username,Player2Username):
        player1GuessingGrid = [["O" for _ in range(9)] for _ in range(9)]
        player2GuessingGrid = [["O" for _ in range(9)] for _ in range(9)]


        player1Hits = {"Carrier" : 0, "Battleship": 0, "Cruiser" : 0, "Submarine" : 0, "Destroyer" : 0, "Total": 0 }
        player2Hits = {"Carrier" : 0, "Battleship": 0, "Cruiser" : 0, "Submarine" : 0, "Destroyer" : 0, "Total": 0 }

        turn = "Player 1"
        winner = ""

        while winner == "":
            if turn == "Player 1":
                player1GuessingGrid = GuessingLocation.guessLocation(player2Grid,player1GuessingGrid,player1Hits,Player1Username)
                turn = "Player 2"
                winner = GuessingLocation.isWinner(player1Hits,turn)
            else:
                player2GuessingGrid = GuessingLocation.guessLocation(player1Grid,player2GuessingGrid,player2Hits,Player2Username)
                turn = "Player 1"
                winner = GuessingLocation.isWinner(player2Hits,turn)


        return winner
            