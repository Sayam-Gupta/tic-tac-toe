# These are all the functions

# Shows the board

def display_board(board):
  print(board[7]+' | '+board[8]+' | '+board[9])
  print('--|---|--')
  print(board[4]+' | '+board[5]+' | '+board[6])
  print('--|---|--')
  print(board[1]+' | '+board[2]+' | '+board[3])
  
# This makes the player input which marker they want
  
def player_input():
  marker = ''
  while not (marker == 'X' or marker == 'O'):
       marker = input('Player 1: Do you want to be X or O? ').upper()
  if marker == 'X':
    return ('X', 'O')
    print('player 1 is X and player 2 is O')
  else:
    return ('O', 'X')
    print('Player 1 is O and plauer 2 is X')

# Asks the player where they want their marker placed
        
def place_marker(board, marker,position):
  i = int(position)
  board[i] = marker
  
# Checks if a player has won
  
def win_check(board,marker):
  return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
  (board[4] == marker and board[5] == marker and board[6] == marker) or 
  (board[7] == marker and board[8] == marker and board[9] == marker) or 
  (board[1] == marker and board[4] == marker and board[7] == marker) or 
  (board[2] == marker and board[5] == marker and board[8] == marker) or
  (board[3] == marker and board[6] == marker and board[9] == marker) or 
  (board[1] == marker and board[5] == marker and board[9] == marker) or 
  (board[3] == marker and board[5] == marker and board[7] == marker))
  
# Chooses from random which player goes first
  
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Checks if there is a place left where the person wants to move

def space_check(board, position):
  i = int(position)
  return board[i] == ' '
  
 # Checks if the board is full
  
def full_board_check(board):
  for i in range(1,10):
    if space_check(board,i):
      return False
  return True
  
# This functions asks the player to input a number where he wants to move

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
      position = int(input('Choose your next position: (1-9) '))
    return position
    
# This function returns a boolean when asked to to play again
  
def replay():
  ans = ''
  ans = input('Do you want to play again').lower()
  if ans == 'yes':
    return True
  
# This is the main script
#############################

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    playboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    playgame = input('Are you ready to play? Enter Yes or No.')
    
    if playgame.lower()[0] == 'y':
        gameplay = True
    else:
        gameplay = False

    while gameplay:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(playboard)
            position = player_choice(playboard)
            place_marker(playboard, player1_marker, position)

            if win_check(playboard, player1_marker):
                display_board(playboard)
                print('Congratulations Player1! You have won the game!')
                gameplay = False
            else:
                if full_board_check(playboard):
                    display_board(playboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
        else:
            # Player2's turn.
            
            display_board(playboard)
            position = player_choice(playboard)
            place_marker(playboard, player2_marker, position)

            if win_check(playboard, player2_marker):
                display_board(playboard)
                print('Congratulation Player 2! You have won the game!')
                gameplay = False
            else:
                if full_board_check(playboard):
                    display_board(playboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
 