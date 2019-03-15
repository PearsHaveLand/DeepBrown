EMPTY_SPACE = ' '
VERTICAL_EDGE = "-----------------"
HORIZONTAL_EDGE = '|'
BOTTOM_LABEL = "  1 2 3 4 5 6 7"
NUM_ROWS = 6
NUM_COLS = 7

# helper for quickly printing list contents without the rest of the list
def list_contents(list):
    ret = ' '
    for item in list:
        ret += str(item) + ' '
    return ret

class deepbrown(object):
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
    def checkWin(self, tile):

        board = self.m_board

        # check horizontal spaces
        for y in range(NUM_ROWS):
            for x in range(NUM_COLS - 3):
                if board[x][y] == tile and board[x+1][y] == tile and \
                board[x+2][y] == tile and board[x+3][y] == tile:
                    return True

        # check vertical spaces
        for x in range(NUM_COLS):
            for y in range(NUM_ROWS - 3):
                if board[x][y] == tile and board[x][y+1] == tile and \
                board[x][y+2] == tile and board[x][y+3] == tile:
                    return True

        # check / diagonal spaces
        for x in range(NUM_COLS - 3):
            for y in range(3, NUM_ROWS):
                if board[x][y] == tile and board[x+1][y-1] == tile and \
                board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                    return True

        # check \ diagonal spaces
        for x in range(NUM_COLS - 3):
            for y in range(NUM_ROWS - 3):
                if board[x][y] == tile and board[x+1][y+1] == tile and \
                board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                    return True

        return False

    # TODO: Implement brown_move
    def brown_move(self):

    # TODO: Implement player_move
    def player_move(self):

    def run_game(self, brown_first=False):
        player_wins = False
        brown_wins = False

        if brown_first:
            brown_wins = brown_move()

        while not brown_wins and not player_wins:
            player_wins = player_move()

            if player_wins:
                break

            brown_wins = brown_move()

brown = deepbrown()
brown.display_board()
