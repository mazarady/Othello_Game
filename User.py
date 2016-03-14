#Maaz Munir
#22602418
import games
import instruct

def user_input() -> int and input:
       '''asks  user to input number of rows and columns
       and takes in whose turn it is going to be and what peice
       should it be, top left'''

       rows = int(input('Rows. Even number, 4-16: ' ))
       columns = int(input('Columns. Even number, 4-16: '))
       whose_turn = input('Who Goes First: B or W: ')
       top_left = input('Who is the Top Left Piece, B or W: ')
       winner = input('Win by >(Greater Than) or < (Less Than): ')
       print()
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
       
       print('INVALID MOVE')
       print('TRY AGAIN')
       
def valid():
       '''prints Valid '''
       
       print('VALID')

def user_total(x, y):
       '''prints user total'''
       
       print('W:', x, end = ' ')
       print('B:', y)


              
def make_move() -> int:
       '''takes in input for rows and columns user wishes to place'''
       row = int(input('Row: '))
       col = int(input('Column: '))
       

       
       return row -1, col-1
def main():
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
       try:
     
              print('Welcome to Othello')
              print('Press 1 if you would like to read the instructions: ')
              print('Press 2 if you already know how to play: ')
              enter = int(input(''))
              if enter == 1:
                     instruct.print_instruct()
                     main()
                     
              elif enter == 2:
                     main()
       except:
              pass
                     



              
              
              
              
              
       
   
              


       
             

     

          
              

    
              

             
                            
                     
              

              
              
              
       
              
              
              


       

       
       


       
       

       
