global variables

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_runs = True
winner = None
current_player = "X"

def _play_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    _play_board()

    while game_runs:
        _handle_turn(current_player)
        game_over()
        _switch_player()


    if winner == "X" or winner == "0":
        print(winner, 'you won!')
    elif winner == None:
     print('its a Tie!')


def _handle_turn(player):
    print(player, 'turn')
    place = input('choose place from 1-9: ')

    valid = False
    while not valid:
        while place not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            place = input('choose place from 1-9: ')

        place = int(place)-1

        if board[place] == "_":
            valid = True
        else:
            print('taken spot,try again')

    board[place] = player

    _play_board()

def game_over():
    _check_winner()
    _check_tie()

def _check_winner():
    global winner

    raw_winner = _check_rows()
    columns_winner = _check_columns()
    diagonals_winner = _check_diagonals()

    if raw_winner:
        winner = raw_winner
    elif columns_winner:
        winner = columns_winner
    elif diagonals_winner:
        winner = diagonals_winner
    else:
        winner = None
    return




def _check_rows():
    global game_runs
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_runs = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def _check_columns():
    global game_runs
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1 or column_2 or column_3:
        game_runs = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def _check_diagonals():
    global game_runs
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"
    if diagonal_1 or diagonal_2:
        game_runs = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return



def _check_tie():
    global game_runs
    if "_" not in board:
        game_runs = False
        return


def _switch_player():

    global current_player

    if current_player == "X":
       current_player = "0"
    elif current_player == "0":
      current_player = "X"
    return

play_game()



