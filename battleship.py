from random import randint

board_size = 5
board = []
# ship = [start_row, start_col, orientation, size]
ship = []
ship_row = []
ship_col = []
ship_size = 3
ships = ((4, 1), (3, 1), (2, 1), (1, 2))

for x in range(board_size):
  board.append(["O"] * board_size)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def one_ship (s_size, board):
    orient = randint (0, 1)
    start_row = random_row(board)
    start_col = random_col(board)

    while ((start_row + s_size) > len(board) or (start_col + s_size) > len(board)):
        orient = randint (0, 1)
        start_row = random_row(board)
        start_col = random_col(board)

    return (start_row, start_col, orient, s_size)

def add_ship (ship, s_row, s_col):
    step = 0
    for i in range(ship[3]):
      if ship[2] == 0:
        s_row.append (ship[0])
        s_col.append (ship[1] + step)
        step += 1
      elif ship[2] == 1:
        s_row.append (ship[0] + step)
        s_col.append (ship[1])
        step += 1

def hit_ship (ship, ship_row,ship_col, guess_row, guess_col):
    f = False
    for i in range (ship[3]):
        if guess_row == ship_row[i] and guess_col == ship_col[i]:
            print "You hit my battleship."
            board[guess_row][guess_col] = "*"
            print_board(board)
            f = True
    return f



#ship_row = random_row(board)
#ship_col = random_col(board)
ship = one_ship (ship_size, board)
#ship_row.append (ship[0])
#ship_col.append (ship[1])
add_ship (ship, ship_row, ship_col)

#debagging
#print range(ship[3]-1)
print ship
print ship_row ,
print ship_col

turns = int(raw_input("How much turns do you want?"))

for turn in range(turns):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if hit_ship (ship, ship_row,ship_col, guess_row, guess_col) == False:
    if (guess_row < 0 or guess_row > board_size - 1) or (guess_col < 0 or guess_col > board_size - 1):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      print_board(board)

  if turn == turns - 1:
    print "Game Over"

print

for i in range(ship[3]):
    if board[ship_row[i]][ship_col[i]] != '*':
        board[ship_row[i]][ship_col[i]] = "S"

print "Here is the ship!"
print_board(board)
