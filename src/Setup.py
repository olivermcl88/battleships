class Setup():
    def validateCoOrdinate(choice):
        if choice >=0 and choice <=8:
            return True
        else:
            return False
        
    def isShipAlreadyThere(xBottomChoice,yBottomChoice,xTopChoice,yTopChoice,grid,length):
        valid = True

        if (xTopChoice - xBottomChoice) == 0 and (yTopChoice - yBottomChoice) == (length-1):
            while xBottomChoice <= xTopChoice and valid == True:
                if grid[yBottomChoice][xBottomChoice] != "Empty":
                    valid = False
                else:
                    xBottomChoice += 1
        elif (xTopChoice - xBottomChoice) == (length-1) and (yTopChoice - yBottomChoice) == 0:
            while yBottomChoice <= yTopChoice and valid == True:
                if grid[yBottomChoice][xBottomChoice] != "Empty":
                    valid = False
                else:
                     yBottomChoice += 1
        else: 
            valid = False

        return valid

    def validateChoice(name,length,xBottomChoice,yBottomChoice,xTopChoice,yTopChoice,grid):
        if Setup.validateCoOrdinate(xBottomChoice) and Setup.validateCoOrdinate(xTopChoice) and Setup.validateCoOrdinate(yBottomChoice) and Setup.validateCoOrdinate(yTopChoice):
                if Setup.isShipAlreadyThere(xBottomChoice,yBottomChoice,xTopChoice,yTopChoice,grid,length):
                    return True

        return False
    
    def placeBoat(name,length,xBottomChoice,yBottomChoice,xTopChoice,grid):
        if (xBottomChoice - xTopChoice) == 0 :
            counter = yBottomChoice
            while counter <= length:
                grid[counter][xBottomChoice] = name
                counter += 1
        else:
            counter = xBottomChoice
            while counter <= length:
                grid[yBottomChoice][counter] = name
                counter += 1

    def displayGrid(grid):
        # Print column headers with adjusted spacing to align with the grid
        column_headers_spacing = " " * 12
        for i in range(len(grid[0])):
            column_headers = " "* 3 + str(i+1)  + " "* 3
            print(column_headers, end=" ")

        # Separator line
        print("\n   " + "-" * (len(grid[0]) * 8 ))

        # Print each row with row index
        for index, row in enumerate(grid):
            row_str = f"{index+1} | " + " | ".join(row)
            print(row_str)
            print("   " + "-" * (len(row_str) - 1))

    def pickBoatPosition(username):
        rows = 9
        cols = 9
        grid = [["Empty" for _ in range(cols)] for _ in range(rows)]
        
        shipName = ["Carrier", "Battleship", "Cruiser", "Submarine", "Destroyer"]

        for ship in shipName:
            valid = False
            Setup.displayGrid(grid)

            while valid == False:
                xBottomChoice = int(input(f"{username}, what is the x position of where you would like to place the bottom of the {ship}: "))-1
                yBottomChoice = int(input((f"{username}, what is the y position of where you would like to place the bottom of the {ship}: ")))-1

                xTopChoice = int(input(f"{username}, what is the x position of where you would like to place the top of the {ship}: "))-1
                yTopChoice = int(input(f"{username}, what is the y position of where you would like to place the top of the {ship}: "))-1

                if ship == "Carrier":
                    length = 5
                elif ship == "Battleship":
                    length = 4
                elif ship == "Cruiser" or ship == "Submarine":
                    length = 3
                else:
                    length = 2

                valid = Setup.validateChoice(ship,length,xBottomChoice,yBottomChoice,xTopChoice,yTopChoice,grid) 

                if valid == True:
                    Setup.placeBoat(ship,length,xBottomChoice,yBottomChoice,xTopChoice,grid)
                else:
                    print("\nIncorrect values entered for size of ship. The ship is of size " + str(length))
                    print("Also remember where you have placed prior ships\n")
        
        return grid