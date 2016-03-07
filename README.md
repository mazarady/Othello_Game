# Othello_Game
Game Logic and User Interface of the Game Othello

import User
import collections

NONE = 0
WHITE = 1
BLACK = 2
DIR = [(1,0),(-1,-1),(0,-1),(1,-1),(-1,0),(1,1),(0,1),(-1,1)]

class InvalidMoveError(Exception):
       '''player makes  move outside the scope'''
       pass
class IndexError(Exception):
       '''if player makes move outside of scope'''
       pass

class game:
       '''First class that has a create attribute, places default pieces, calculates total
and determines the winnner'''
       
       def __init__(self, rows, columns, top_left, winner):
              self.rows = rows
              self.columns = columns
              self.top_left = top_left
              self.board = []
              self.winner = winner


       def create(self) -> [[int]]:
              '''creates 2 dimensional list'''
                          
              for row in range(self.rows):
                     self.board.append([])
                     for col in range(self.columns):
                            self.board[-1].append(NONE)
              return self.board
                            
       def put_peece(self) -> None:
              '''places default pieces according to which user wanted the top
              left piece will be'''
       
              
              if self.top_left == 'B':
                            
                     self.board[int(self.rows/2) -1][int(self.columns/2)-1] = BLACK
                     self.board[int(self.rows/2)][int(self.columns/2)] = BLACK
                     self.board[int(self.rows/2)][int(self.columns/2)-1] = WHITE
                     self.board[int(self.rows/2)-1][int(self.columns/2)] = WHITE
                     
              elif self.top_left == 'W':
                     
                     self.board[int(self.rows/2) -1][int(self.columns/2)-1] = WHITE
                     self.board[int(self.rows/2)][int(self.columns/2)] = WHITE
                     self.board[int(self.rows/2)][int(self.columns/2)-1] = BLACK
                     self.board[int(self.rows/2)-1][int(self.columns/2)] = BLACK

       def total(self) -> int:
              '''calculates the total pieces on the board'''
       
              self.white_total = 0
              self.black_total = 0
              
              
              for sublist in self.board:
                     for element in sublist:
                            if element == 1:
                                   self.white_total += 1
                            elif element == 2:
                                   self.black_total += 1
                                   
              return self.white_total, self.black_total
       
       def win(self) -> None:
              ''' Decides The Winner'''

              if self.winner == '>':
                     if self.black_total > self.white_total:
                            User.black_winner()
                     elif self.white_total > self.black_total:
                            User.white_winner()
                     else:
                            User.tie_winner()

              elif self.winner == '<':
                     if self.black_total < self.white_total:
                            User.black_winner()
                     elif self.white_total < self.black_total:
                            User.white_winner()
                     else:
                            User.tie_winner()


class place:
       def __init__(self, row_move, col_move, board, whose_turn, rows, columns):
                           
              self.row_move = row_move
              self.col_move = col_move
              self.board = board
              self.whose_turn = whose_turn
              self.rows = rows
              self.columns = columns
              
       def check_location(self, x, y) -> bool:
              '''checks the location of the pieces and makes sure
       nothing falls off the board'''
    
              if x > self.rows-1:
                     
                     return False

                     
              elif x < 0:
                     return False
                    
              elif y > self.columns-1:
                     return False
                     
              elif y< 0:
                     return False
              return True
              

       def left(self) -> bool:
              '''checks left'''
              y = self.col_move
              start_location = y
              end_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              elif self.whose_turn =='B':
                     wt = BLACK
              
              while y > 0:
                     y -= 1
                     
                     if self.board[self.row_move][y] == wt:
                            end_location = y
                            break
                     if self.board[self.row_move][y] == NONE:
                            return False
              
              if start_location +1 == end_location or start_location == end_location:
                     return False
              
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              else:
                     return True

       def right(self) -> bool:
              '''checks right'''
              y = self.col_move
              start_location = y
              end_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              elif self.whose_turn =='B':
                     wt = BLACK
                     
              while y < self.columns - 1:
                     y += 1
                     if self.board[self.row_move][y] == wt:
                            end_location = y
                            break
                     if self.board[self.row_move][y] == NONE:
                            return False
              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              else:
                     return True
                     
       def up(self) -> bool:
              '''checks up'''
              x = self.row_move
              start_location = x
              end_location = x
              
              if self.whose_turn == 'W':
                     wt = WHITE
              elif self.whose_turn =='B':
                     wt = BLACK
              
              while x > 0:
                     x -= 1
                     
                     if self.board[x][self.col_move] == wt:
                            end_location = x
                            break
                            
                     if self.board[x][self.col_move] == NONE:
                            return False
                                                               
              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              else:
                     return True
                     

       def down(self) -> bool:
              '''checks down'''
              x = self.row_move
              start_location = x
              end_location = x
              
              if self.whose_turn == 'W':
                     wt = WHITE
              else:
                     wt = BLACK
                     
              while x < self.rows - 1:
                     x += 1
                     if self.board[x][self.col_move] == wt:
                            end_location = x
                            break
       
                     if self.board[x][self.col_move] == NONE:
                            return False

              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              else:
                     return True

                            
       def right_up(self) -> bool:
              '''checks right_up'''
              x = self.row_move
              y = self.col_move
       
              start_location = x
              end_location = x

              start_y_location = y
              end_y_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              else:
                     wt = BLACK

              while x > 0 and y < self.columns - 1:
                     x -=1
                     y +=1
                     
                     if self.board[x][y] == wt:
                            end_location = x
                            end_y_location = y
                            break
       
                     if self.board[x][y] == NONE:
                            return False

              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_y_location +1 == end_y_location or start_y_location == end_y_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              
              elif start_y_location -1 == end_y_location or start_y_location == end_y_location:
                     return False
              else:
                     return True
       
       def right_down(self) -> bool:
              '''checks right_down'''
              x = self.row_move
              y = self.col_move
       
              start_location = x
              end_location = x

              start_y_location = y
              end_y_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              else:
                     wt = BLACK
              
              while x < self.rows -1 and y < self.columns -1:
                     y += 1
                     x+=1
                     
                     if self.board[x][y] == wt:
                            end_location = x
                            end_y_location = y
                            break
       
                     if self.board[x][y] == NONE:
                            return False

              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_y_location +1 == end_y_location or start_y_location == end_y_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              
              elif start_y_location -1 == end_y_location or start_y_location == end_y_location:
                     return False
              else:
                     return True
              
       def left_up(self) -> bool:
              '''checks left_up'''
              x = self.row_move
              y = self.col_move
       
              start_location = x
              end_location = x

              start_y_location = y
              end_y_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              else:
                     wt = BLACK
              
              while y > 0 and x > 0:
                     y -=1
                     x -=1
                     
                     if self.board[x][y] == wt:
                            end_location = x
                            end_y_location = y
                            break
       
                     if self.board[x][y] == NONE: 
                            return False

              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_y_location +1 == end_y_location or start_y_location == end_y_location:
                     return False
              
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              
              elif start_y_location -1 == end_y_location or start_y_location == end_y_location:
                     return False
              else:
                     return True
              
       def left_down(self) -> bool:
              '''checks left_down'''
              x = self.row_move
              y = self.col_move
       
              start_location = x
              end_location = x

              start_y_location = y
              end_y_location = y
              
              if self.whose_turn == 'W':
                     wt = WHITE
              else:
                     wt = BLACK
              
              while y > 0 and x < self.rows-1:
                     y -=1
                     x +=1
                     
                     if self.board[x][y] == wt:
                            end_location = x
                            end_y_location = y
                            break
       
                     if self.board[x][y] == NONE:
                            return False
              
              
              if start_location +1 == end_location or start_location == end_location:
                     return False
              elif start_y_location +1 == end_y_location or start_y_location == end_y_location:
                     return False
              elif start_location -1 == end_location or start_location == end_location:
                     return False
              
              elif start_y_location -1 == end_y_location or start_y_location == end_y_location:
                     return False
              else:
                     return True
              
       def piss(self) -> bool:
              '''checks piece placed'''
              
              x = self.row_move
              y = self.col_move

              if self.whose_turn == 'W':
                     if self.board[x][y] == WHITE:
                            return False
                     elif self.board[x][y] == BLACK:
                            return False
              elif self.whose_turn == 'B':
                     if self.board[x][y] == BLACK:
                            return False
                     elif self.board[x][y] == WHITE:
                            return False
              elif self.whose_turn == None:
                     return False
              else:
                     return True

              
       def everything(self) -> list:
              '''checks through self.board and adds valid
pieces to the list'''

              valids = []
              
              x = self.row_move
              y = self.col_move

              for row in range(self.rows):
                    for col in range(self.columns):
                           if self.board[row][col] == 0:
                                  self.row_move = row
                                  self.col_move = col
                                 
                                  if self.valid_position():
                                         self.row_move = x
                                         self.col_move = y
                                         valids.append([x,y])
                                         return valids
                                   
              self.row_move = x
              self.col_move = y
              return valids
                            
       def valid_position(self) -> bool:
              '''returns either true or false depending on the valid locations'''
              return self.piss() or self.up() or self.down() or self.left() or self.right() or self.right_up() or self.left_down() or self.left_up() or self.right_down()

       def are_there_moves_left(self) -> bool:
              
              '''checks to see if there are moves left'''
              valid = set()
              for item in self.board:
                     for element in item:
                            valid.add(element)

                     
              if NONE in valid:
                     if self.valid_position() == True:
                            return True
                     elif self.valid_position() == False:
                            self.opp_turn()
                            return self.opp_turn()
              else:
                     return False


       def opp_turn(self) -> str:
              '''returns the opposite turn'''
              
              if self.whose_turn == 'W':
                     self.whose_turn = 'B'
                     return self.whose_turn

              elif self.whose_turn == 'B':
                     self.whose_turn = 'W'
                     return self.whose_turn
              
       def same_turn(self) -> str:
              '''just returns the same turn'''
              
              if self.whose_turn == 'W':
                     self.whose_turn = 'W'
                     return self.whose_turn
              elif self.whose_turn == 'B':
                     self.whose_turn = 'B'
                     return self.whose_turn
              
       def makes_move(self) -> str:
              '''makes the move and also turns it'''
              x = self.everything()
              if len(x) > 0:
                     
                     if self.are_there_moves_left():
                                   
                     
                            if self.valid_position() and self.board[self.row_move][self.col_move] == NONE:
                                   
                                   User.valid()
                                   if self.whose_turn == 'W':
                                          self.board[self.row_move][self.col_move] = WHITE
                                          
                                          for rowz, colz in DIR:
                                                 turn_x = self.row_move
                                                 turn_y = self.col_move
                                   
                                                 turn_updated_x = rowz + turn_x
                                                 turn_updated_y = colz + turn_y
                            
                                                  
                                                 if self.check_location(turn_updated_x, turn_updated_y) and self.board[turn_updated_x][turn_updated_y] == BLACK:
                                                        storage = []

                                                        while True:
                                                               if not self.check_location(turn_x, turn_y):
                                                                      break

                                                               elif self.board[turn_x][turn_y] == BLACK:
                                                                      storage.append((turn_x, turn_y))
                                                                      pass
                                                               elif self.board[turn_x][turn_y] == WHITE:
                                                                      for element in storage:
                                                                             self.board[element[0]][element[1]] = WHITE
                                                                             
                                                                             
                                                               turn_x+= rowz
                                                               turn_y += colz
                                   

                                          
                                   elif self.whose_turn == 'B':
                                          self.board[self.row_move][self.col_move] = BLACK
                                                        
                                          for black_rowz, black_colz in DIR:
                                                 black_x = self.row_move
                                                 black_y = self.col_move
                                                 
                                                 new_x = black_x + black_rowz
                                                 new_y = black_y + black_colz
                                                 
                                                 if self.check_location(new_x, new_y) and self.board[new_x][new_y] == WHITE:
                                                        storage = []

                                                        while True:
                                                               
                                                               if not self.check_location(black_x,black_y):
                                                                      break
                                                                      
                                                               elif self.board[black_x][black_y] == WHITE:
                                                                      storage.append( (black_x, black_y))
                                                                      pass
                                                                      
                                                                      
                                                               elif  self.board[black_x][black_y] == BLACK:
                                                                      for item in storage:
                                                                             self.board[item[0]][item[1]] = BLACK                                                                             
                                                               black_x += black_rowz
                                                               black_y += black_colz
                                   
                                   self.opp_turn()
                                   return self.whose_turn

                                   
                            else:
                                   User.not_valid()
                                   self.same_turn()
                                   return self.whose_turn
                     else:
                            self.opp_turn()
                            return self.whose_turn
                     
                                   
              else:
                     self.opp_turn()
                     return self.whose_turn
                     
                     
                     
## New FILE THIS IS THE USER INTERFACE. THIS IS THE PROGRAM YOU RUN THE CODE ABOVE IS THE GAME LOGIC             
import games

def user_input() -> int and input:
       '''asks  user to input number of rows and columns
       and takes in whose turn it is going to be and what peice
       should it be, top left'''

       rows = int(input('' ))
       columns = int(input(''))
       whose_turn = input('')
       top_left = input('')
       winner = input('')
       return rows, columns, whose_turn, top_left, winner


def game_board(columns, rows, board):
       '''this function is to display the game board'''

       for row in range(rows):
              for col in range(columns):
                                                                                                      
                     if board[row][col] == games.NONE:
                            print('.', end = ' ')
                     elif board[row][col] == games.WHITE:
                            print('W', end = ' ')
                     elif board[row][col] == games.BLACK:
                            print('B', end = ' ')
              print()

                           
def black_winner():
       '''prints the black winner'''
       print('WINNER: BLACK')

def white_winner():
       '''prints the white winner'''
       
       print('WINNER: WHITE')
       
def tie_winner():
       '''prints tie '''

       print('WINNER: NONE')
       
def not_valid():
       '''prints Invalid '''
       
       print('INVALID')
       
def valid():
       '''prints Valid '''
       
       print('VALID')

def user_total(x, y):
       '''prints user total'''
       
       print('W:', x, end = ' ')
       print('B:', y)


              
def make_move() -> int:
       '''takes in input for rows and columns user wishes to place'''
       row_col = input('')
       l = row_col.split()
       
       row = int(l[0])
       col = int(l[1])
       
       return row -1, col-1
def main():
       
       print('FULL')
       rows, columns, whose_turn, top_left, winner= user_input()
       board = games.game(rows, columns, top_left, winner)
       board.create()
       board.put_peece()
       x, y = board.total()
       user_total(x, y)
       rows_columns = game_board(columns, rows, board.board)
       print('TURN:', whose_turn)
       row_move, col_move = make_move()


       while True:
              print()
              updated_board = games.place(row_move, col_move, board.board, whose_turn, board.rows, board.columns)
              whose_turn = updated_board.makes_move()
              x, y = board.total()
              user_total(x,y)
              rows_columns = game_board(columns, rows, board.board)

              if updated_board.are_there_moves_left():
                                          
                     if len(updated_board.everything()) > 0:
                            print('TURN:', whose_turn)
                            row_move, col_move = make_move()
                     
                     elif len(updated_board.everything()) < 0:
                            print()
                            updated_board.opp_turn()
                            print('TURN:', whose_turn)
                            print()
              else:
                     
                     board.win()
                     break

              
if __name__ == '__main__':
       main()
