# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 13:08:44 2015
This code coppied/past from internet...
https://inventwithpython.com/
___________________
Invent Your Own
Computer Games 
with Python, 2nd Edition
By Al Sweigart
___________________

Authors of the book has a Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States
License.
http://creativecommons.org/licenses/by-nc-sa/3.0/us/

After download code
updated partially... No quality check
no -- nothing
zip -- 
Use it at your own risk

"""

   # Tic Tac Toe  

import random
import sys
import pdb
   
def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
      
def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player’s letter as the first 
    # item, and the computer's letter as the second.
    letter = ''
    letter=raw_input('Select either X or O to play -> ').upper()
    # the first element in the list is the player’s letter, 
    # the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
      # Randomly choose the player who goes first.
      if random.randint(0, 1) == 0:
          return 'computer'
      else:
          return 'player'
          
def playAgain():
      # This function returns True if the player wants to play again, otherwise it returns False.
      print('Do you want to play again? (yes or no)')
      return input().lower().startswith('y')
      
def makeMove(board, letter, move):
      board[move] = letter
      return board
      
def isWinner(bo, le):
      # Given a board and a player’s letter, this function returns True if that player has won.
      # We use bo instead of board and le instead of letter so we don’t have to type as much.
      return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
      (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
      (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
      (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
      (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
      (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
      (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
      (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
      
def getBoardCopy(board):
      # Make a duplicate of the board list and return it the duplicate.
      dupeBoard = []
      for i in board:
          dupeBoard.append(i)
      return dupeBoard
      
      
def getPlayerMove(board):
    # Let the player type in their move.
    flag = True
    while flag:
        move = raw_input('input your move (1-9)')
        move = int(move)
        if isSpaceFree(board, int(move)):
            break
    return move
      
def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '

def chooseRandomMoveFromList(board, movesList):
      # Returns a valid move from the passed list on the passed board.
      # Returns None if there is no valid move.
      possibleMoves = []
      for i in movesList:
          if isSpaceFree(board, i):
              possibleMoves.append(i)
      if len(possibleMoves) != 0:
          return random.choice(possibleMoves)
      else:
          return None

def isLocationFreeFromList(board, movesList):
      # Returns True or False
      possibleMoves = []
      for i in movesList:
          if isSpaceFree(board, i):
              possibleMoves.append(i)
      if len(possibleMoves) != 0:
          return True 
      else:
          return False

def get_playerletter(computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    return playerLetter

def ComputerCanWin(board, computerLetter):
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return True
    return False


def playerCanWin(board,playerLetter):              
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return True
    return False

def getwinningPosition(board,playerLetter):              
    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

def getComputerMove(board, computerLetter):
    '''
    This function finds the next move of the 
    computer.
    '''
    playerLetter = get_playerletter(computerLetter) #get player letter (either comp or person)

    if ComputerCanWin(board, computerLetter):
        moveto = getwinningPosition(board,playerLetter)
        return moveto
        

    # If player is winning block the position
    if playerCanWin(board,playerLetter):
        moveto = getwinningPosition(board,playerLetter)
        return moveto

    # Try to take one of the corners, if they are free.
    if isLocationFreeFromList(board, [1, 3, 7, 9]):
        moveto = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        return moveto

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        moveto = 5
        return moveto

    if isLocationFreeFromList(board, [2, 4, 6, 8]):
        moveto = chooseRandomMoveFromList(board, [2, 4, 6, 8])
        return moveto


def getComputerMove2(board, computerLetter, count, playerstarts):
    '''
    This function finds the next move of the 
    computer.
    '''
    playerLetter = get_playerletter(computerLetter) #get player letter (either comp or person)


    if playerstarts & count==1:
        if isSpaceFree(board, 5):
            moveto = 5
            return moveto
        else:
            pass


    if ComputerCanWin(board, computerLetter):
        moveto = getwinningPosition(board,playerLetter)
        return moveto
        

    # If player is winning block the position
    if playerCanWin(board,playerLetter):
        moveto = getwinningPosition(board,playerLetter)
        return moveto

    # Try to take one of the corners, if they are free.
    if isLocationFreeFromList(board, [1, 3, 7, 9]):
        moveto = chooseRandomMoveFromList(board, [1, 3, 7, 9])
        return moveto

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        moveto = 5
        return moveto

    if isLocationFreeFromList(board, [2, 4, 6, 8]):
        moveto = chooseRandomMoveFromList(board, [2, 4, 6, 8])
        return moveto




def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.
     for i in range(1, 10):
         if isSpaceFree(board, i):
             return False
     return True
    



if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')

    while True:
        # Reset the board
        theBoard = [' '] * 10
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        if turn == 'player':
            playerstarts = True
        else:
            playerstarts = False 

        print('The ' + turn + ' will go first.')
        #gameIsPlaying = True
        drawBoard(theBoard)
        
        count = 1
        while True:
            if turn == 'player': # Player’s turn.
                move     = getPlayerMove(theBoard) #1,2,3,...,9
                theBoard = makeMove(theBoard, playerLetter, move) #board[move] is updated
                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    break
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'

            else: # Computer’s turn.
                
                print '----------------------'
                print 'Computer playing -----'



                #move = getComputerMove(theBoard, computerLetter)
                move = getComputerMove2(theBoard, computerLetter, count, playerstarts)





                theBoard = makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    print('The computer has beaten you! You lose.')
                    break
                else:
                    if isBoardFull(theBoard):
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
            print 'game -->', count
            drawBoard(theBoard)
            count = count + 1
