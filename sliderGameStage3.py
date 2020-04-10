from random import randint ###Imports the class random for use below

board = [-1, -1, -1, -1], [-1, -1, -1 , -1], [-1, -1, -1, -1], [-1, -1, -1 , -1]

def initializeBoard(): ###Generates the game board
    ###Initialize variables
    x = 0
    y = 0
    count = 1

    while(count < 16): ###Randomly assigns spots in the array whatever the current count is
        x = randint(0,3)
        y = randint(0,3)
        if board[x][y] == -1:
            board[x][y] = count
            count +=1

def playGame():
    ###Initialize variables
    userInput = 0
    userInputRow = -1
    userInputColumn = -1
    emptySpotRow = -1
    emptySpotColumn = -1
    gameOver = False

    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == -1):
                emptySpotRow = x ###Stores the value of the row of the empty spot
                emptySpotColumn = y ###Stores the value of the column of the empty spot
    while(gameOver == False):
        printBoard()
        userInput = checkMove()
        if((userInput > 0) and (userInput < 16)): ###Checks to see if the user entered a valid number
            for x in range(len(board)):
                for y in range(len(board[x])):
                    if(board[x][y] == userInput): ###Finds the value on the board that the user enters
                        userInputRow = x ###Sets the value of the row of the number the user enters
                        userInputColumn = y ###Sets the value of the column of the number the user enters
            if(((emptySpotRow+1 == userInputRow) and (emptySpotColumn == userInputColumn)) or ((emptySpotRow-1 == userInputRow) and (emptySpotColumn == userInputColumn)) or ((emptySpotRow == userInputRow) and (emptySpotColumn+1 == userInputColumn)) or ((emptySpotRow == userInputRow) and (emptySpotColumn-1 == userInputColumn))):
            ###The line above checks to see if the move attempting to be made is valid
                board[emptySpotRow][emptySpotColumn] = userInput ###Sets the value of the empty spot on the board to the number the user enters
                board[userInputRow][userInputColumn] = -1 ###Sets the value of the empty spot on the board to -1
                emptySpotRow = userInputRow ###Sets the row of the number the user enters to the new empty spot
                emptySpotColumn = userInputColumn ###Sets the column of the number the user enters to the new empty spot
            else:
                print("That move is invalid. Please try again")
            
            if((board[0][0] == 1) and (board[0][1] == 2) and (board[0][2] == 3) and (board[0][3] == 4) and (board[1][0] == 5) and (board[1][1] == 6) and (board[1][2] == 7) and (board[1][3] == 8) and (board[2][0] == 9) and (board[2][1] == 10) and (board[2][2] == 11) and (board[2][3] == 12) and (board[3][0] == 13) and (board[3][1] == 14) and (board[3][2] == 15)):
            ###The line above checks for a win (the numbers on the board run from 1-15 with a blank space at the end)
               gameOver = True
               print("You did it!")
        else:
            print("The number must be between 1 and 15.")
            userInput = checkMove() ###Allows the user to type a new number in

def checkMove(): ###Checks to see if the move attempting to be made is a valid number
    uInput = 0
    while True:
        uInput=input("\nPlease enter the number you'd like to slide\n")
        try:
            test = int(uInput) ###This is testing the input to see if it is a number (converts from string to int)
            break;
        except ValueError:
            print("\nPlease enter a number!") ###This is telling the user that they entered an invalid value
            printBoard()
    uInput = int(uInput)###This is type casting the confirmed number value to an int then storing it in a new variable
    return uInput
    

def printDirections(): ###Directions to the game are printed on the screen
    print("\n\n\nWelcome to the slider game!\nThe goal of the game is to move")
    print("the tiles until they read 1-15 with the blank in the 16th spot.")
    print("You may only slide one tile at a time and the only place")
    print("a tile may move to is to the empty spot.\n")

def printBoard(): ###The current board is printed on the screen
    for x in range(len(board)):
        for y in range(len(board[x])):
            if(board[x][y] == -1):
                print("  ",end='|')
            elif(board[x][y] < 10):
                print("",board[x][y],end='|')
            else:
                print(board[x][y], end='|')
        print("")

def main(): ###Defines the main methods of the program
    printDirections()
    initializeBoard()
    playGame()

main() ###Runs the main methods of the program
