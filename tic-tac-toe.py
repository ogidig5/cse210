# Author Name: George Ogidi Ochieng
# Assignment: Tic-Tac-Toe Game. Programming with classes

import random

play_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
# Global Variables

currentPlayer = "X"
champion = None
gameOn = True

def main():
  while gameOn:
    drawBoard(play_board)
    playerInput(play_board)
    checkWinner()
    draw(play_board)
    playerSwitch()
    '''computer(play_board)
    checkWinner()
    draw(play_board)'''

# This function draws the Game Play Board
def drawBoard(play_board):
  print(play_board[0] + " | " + play_board[1] + " | " + play_board[2])
  print(play_board[3] + " | " + play_board[4] + " | " + play_board[5])
  print(play_board[6] + " | " + play_board[7] + " | " + play_board[8])
  print()

# Take player input
def playerInput(play_board):
  inp = int(input("Enter a number 1-9: "))
  if inp >= 1 and inp <= 9 and play_board[inp-1] == "-":
    play_board[inp-1] = currentPlayer
  else:
    print("Sorry. A player is already in that spot!")

# Check win or tie
def checkHorizontal(play_board):
  global champion
  if play_board[0] == play_board[1] == play_board[2] and play_board[1] != "-":
    champion = play_board[0]
    return True
  elif play_board[3] == play_board[4] == play_board[5] and play_board[3] != "-":
    champion = play_board[3]
    return True
  elif play_board[6] == play_board[7] == play_board[8] and play_board[6] != "-":
    champion = play_board[6]
    return True

def checkRow(play_board):
  global champion
  if play_board[0] == play_board[3] == play_board[6] and play_board[0] != "-":
    champion = play_board[0]
    return True
  elif play_board[1] == play_board[4] == play_board[7] and play_board[1] != "-":
    champion = play_board[1]
    return True
  elif play_board[2] == play_board[5] == play_board[8] and play_board[2] != "-":
    champion = play_board[2]
    return True

def checkDiagonal(play_board):
  global champion
  if play_board[0] == play_board[4] == play_board[8] and play_board[0] != "-":
    champion = play_board[0]
    return True
  elif play_board[2] == play_board[4] == play_board[6] and play_board[2] != "-":
    champion = play_board[2]
    return True


# Check if there is a tie
def draw(play_board):
  global gameOn
  if "-" not in play_board:
    drawBoard(play_board)
    print("It is a tie!")
    gameOn = False

# Switch the player
def playerSwitch():
  global currentPlayer
  if currentPlayer == "X":
    currentPlayer = "O"
  else:
    currentPlayer = "X"

#  If computer plays against the user. You import the Random module.
'''def computer(play_board):
  while currentPlayer == "O":
    position = random.randint(0, 8)
    if play_board[position] == "-":
      play_board[position] = "O"
      playerSwitch()'''

def checkWinner():
  global gameOn
  if checkDiagonal(play_board) or checkHorizontal(play_board) or checkRow(play_board):   
    print(f"The champion is {champion}") 
    gameOn = False

    
if __name__ == "__main__":
  main()
