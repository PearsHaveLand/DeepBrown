EMPTY_SPACE = ' '
VERTICAL_EDGE = "-----------------"
HORIZONTAL_EDGE = '|'
BOTTOM_LABEL = "  1 2 3 4 5 6 7"
NUM_ROWS = 6
NUM_COLS = 7
PLAYER_CHAR = 'X'
blue_CHAR = 'O'

# helper for quickly printing list contents without the rest of the list
def list_contents(list):
    ret = ' '
    for item in list:
        ret += str(item) + ' '
    return ret

class flatblue(object):
    def __init__(self):
        # initialize game board
        self.m_board = []

        # for each row, create a new empty row
        for i in range(NUM_ROWS):
            row = []

            # fill each row with empty spaces, then append to board
            for i in range(NUM_COLS):
                row.append(EMPTY_SPACE)
            self.m_board.append(row)

    # prints the board to the screen
    def display_board(self):
        print(VERTICAL_EDGE)

        # print board in reverse, since row 0 would be output first
        #   keeping row 0 at the bottom helps me keep my sanity
        for row in reversed(self.m_board):
            print(HORIZONTAL_EDGE, list_contents(row), HORIZONTAL_EDGE, sep='')
        print(VERTICAL_EDGE)
        print(BOTTOM_LABEL)

    # attempts to place a piece of the given character into the given column
    # relies on exterior functions to check for error values
    def place_piece(self, player_char, col):
        row = NUM_ROWS - 1
        placed = False

        # Look through each row in the column
        while (row >= 0) and (not placed):
            # When not at the bottom, need to account for space below
            if row > 0:
                if self.m_board[row][col] == EMPTY_SPACE and self.m_board[row-1][col] != EMPTY_SPACE:
                    self.m_board[row][col] = player_char
                    placed = True
            # When at bottom, only need to account current space
            elif row == 0:
                if self.m_board[row][col] == EMPTY_SPACE:
                    self.m_board[row][col] = player_char
                    placed = True
            row -= 1
        return placed

    # Literally stole this function from StackOverflow because I'm lazy and not
    # trying to create a Connect-4 simulator. I'm revolutionizing AI!
    # So credit to Matthew Hanson and SuperBiasedMan
    # link: https://stackoverflow.com/questions/29949169/python-connect-4-check-win-function
    def check_win(self, tile):

        board = self.m_board

        # check horizontal spaces
        for y in range(NUM_ROWS):
            for x in range(NUM_COLS - 3):
                if board[y][x] == tile and board[y][x+1] == tile and \
                board[y][x+2] == tile and board[y][x+3] == tile:
                    return True

        # check vertical spaces
        for x in range(NUM_COLS):
            for y in range(NUM_ROWS - 3):
                if board[y][x] == tile and board[y+1][x] == tile and \
                board[y+2][x] == tile and board[y+3][x] == tile:
                    return True

        # check / diagonal spaces
        for x in range(NUM_COLS - 3):
            for y in range(3, NUM_ROWS):
                if board[y][x] == tile and board[y-1][x+1] == tile and \
                board[y-2][x+2] == tile and board[y-3][x+3] == tile:
                    return True

        # check \ diagonal spaces
        for x in range(NUM_COLS - 3):
            for y in range(NUM_ROWS - 3):
                if board[y][x] == tile and board[y+1][x+1] == tile and \
                board[y+2][x+2] == tile and board[y+3][x+3] == tile:
                    return True

        return False

    # TODO: Implement blue_move
    def blue_move(self):
        return

    def prompt_input(self):
        user_input = -1

        # Until the user inputs a valid column digit, keep prompting
        while user_input < 1 or user_input > NUM_COLS:
            try:
                user_input = int(input("Enter the column number to drop your piece: "))

            # If the user enters a string, handle gracefully
            except ValueError:
                user_input = -1
        # Subtract 1 to use column as index
        return user_input - 1

    # Check if the topmost row in the column is valid
    def check_col(self, col):
        valid = False

        # If topomost space is empty, the column is valid for placement
        if self.m_board[NUM_ROWS - 1][col] == EMPTY_SPACE:
            valid = True
        return valid

    # Handles input prompting and handling, as well as the logic for valid column choice
    def player_move(self):
        valid_col = False
        chosen_col = -1

        # Continually prompt user for input until valid column with space is entered
        while not valid_col:
            chosen_col = self.prompt_input()
            valid_col = self.check_col(chosen_col)
            if not valid_col:
                print("Chosen column is full, choose a different column.")

        # Column choice is valid, a victory test
        self.place_piece(PLAYER_CHAR, chosen_col)
        return self.check_win(PLAYER_CHAR)

    def run_game(self, blue_first=False):
        player_wins = False
        blue_wins = False

        if blue_first:
            blue_wins = blue_move()

        while not blue_wins and not player_wins:
            self.display_board()
            player_wins = self.player_move()

            if player_wins:
                break

            blue_wins = self.blue_move()

        self.display_board()
        if player_wins:
            print("You win!")
        if blue_wins:
            print("You lose.")

blue = flatblue()
blue.run_game()
