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

guy = deepbrown()
guy.display_board()
