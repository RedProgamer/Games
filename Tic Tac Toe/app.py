# --------------------------- Tic-Tac-Toe ---------------------------

# ---- Global variable ----
game_running = True  # assumes whether the game is over or not
current_player = "X"  # assumes who is the current player

# -- board --
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Win ? or Tie
winner = None


# -- display the board --
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# the function will play the game
def play_game():
    # display the interface of the board
    display_board()
    # handle the position given by the player (either X or 0)
    while game_running:
        handle_player(current_player)
        # check is the game is over by checking for the winner or tie
        check_if_game_over()
        # if the current player is X then this function changes to O and vice verse
        switch_player()

        # if the game ends
    if winner == "X" or winner == "O":
        print(f"{winner} won.")
    elif winner is None:
        print("Tie.")


# handle the position input given by the user
def handle_player(player):
    print(f"{player}'s turn")
    position = input("Choose a number from 1-9 : ")  # taking the input from the user

    # this loop check if the user has entered a proper value or not
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:  # checks if the user input is within this list
            position = input("Invalid call, Choose from 1-9 : ")

        position = int(position) - 1  # adjusting the value for the board

        if board[position] == "-":
            valid = True
        else:
            print("Please stop messing around")  # warning message

    # inserts X or O, in the given position by the user/player
    board[position] = player
    display_board()  # shows the changes that are done to the board


def check_if_game_over():
    check_for_winner()  # check who is the winner
    check_if_tie()  # check if there is a tie
    return


def check_for_winner():
    global winner

    # check row
    row_winner = check_row()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


# check the rows of the grid for an possible chances
def check_row():
    global game_running

    # check each and every row
    row_1 = board[0] == board[1] == board[2] != "-"  # first row
    row_2 = board[3] == board[4] == board[5] != "-"  # second row
    row_3 = board[6] == board[7] == board[8] != "-"  # third row

    if row_1 or row_2 or row_3:
        game_running = False  # stops the game
    if row_1:
        return board[0]  # return the value of board[0]
    elif row_2:
        return board[3]  # return the value of board[3]
    elif row_3:
        return board[6]  # return the value of board[6]
    return


# check the columns of the grid for any possible match
def check_columns():
    global game_running

    columns_1 = board[0] == board[3] == board[6] != "-"  # first column
    columns_2 = board[1] == board[4] == board[7] != "-"  # second column
    columns_3 = board[2] == board[5] == board[8] != "-"  # third column

    if columns_1 or columns_2 or columns_3:
        game_running = False  # stops the game
    if columns_1:
        return board[0]  # return the value of board[0]
    elif columns_2:
        return board[1]  # return the value of board[3]
    elif columns_3:
        return board[2]
    return


# check the diagonals in the grid for any possible match
def check_diagonals():
    global game_running

    diagonals_1 = board[0] == board[4] == board[8] != "-"  # first diagonal
    diagonals_2 = board[2] == board[4] == board[6] != "-"  # second diagonal

    if diagonals_1 or diagonals_2:
        game_running = False  # stops the game
    if diagonals_1:
        return board[0]  # return the value of board[0]
    elif diagonals_2:
        return board[2]  # return the value of board[3]
    return


# check whether there is a tie or not
def check_if_tie():
    global game_running

    if "-" not in board:
        game_running = False
        print("Tie.")
    return


# change the turn of the players
def switch_player():
    global current_player

    # switch player to "0"
    if current_player == "X":
        current_player = "O"
    # switch player to "X"
    elif current_player == "O":
        current_player = "X"


play_game()
