# TODO:

DEFAULT_DOMAIN = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class Square:
    def __init__(self, domain):
        self.domain = domain

    def __repr__(self):
        return str(self.domain)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.domain == other.domain
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.domain != other.domain
        return True

    def getDomain(self):
        return self.domain


class Puzzle:
    def __init__(self, board, constraints):
        # list of squares
        self.board = board
        # List of constraints. Assumed to be != in the form of board coordinates
        # ((Row, Col), (Row,Col))
        self.constraints = constraints

    def __repr__(self):
        shows = "Squares: " + str(self.squares) + \
            "\nConstraints:" + str(self.constraints)
        return shows

    def print_board(self):
        print("Sudoku Puzzle")
        for r_num in range(len(self.board)):
            if r_num != 0:
                print()
            for c_num in range(len(self.board)):
                square = self.board[r_num][c_num]
                cur_domain = square.getDomain()
                if c_num != 0:
                    print(" ", end="")
                if len(cur_domain) != 1:
                    print(0, end="")
                else:
                    print(cur_domain[0], end="")
                if c_num % 3 == 2:
                    if c_num != len(self.board) - 1:
                        print(" |", end="")
                    elif r_num % 3 == 2 and r_num != len(self.board) - 1:
                        print("\n------+-------+------", end="")
        print()


def parse_input(txt_file):
    file_buf = open(txt_file, "r")
    board = []

    # Parses the text file into a 2D list
    for i in range(9):
        # Row
        line = file_buf.readline().split(' ')
        board.append([])
        for j in range(9):
            # Col
            if line[j] == "0":
                board[i].append(Square(DEFAULT_DOMAIN))
            else:
                board[i].append(Square([int(line[j])]))

    # Constraint is assumed to be !=
    constraints = set()

    # Accounts for the row and column constraints
    board_size = len(board)
    for row_num in range(board_size):
        for col_num in range(board_size):
            for i in range(board_size):
                if col_num != i:
                    constraints.add(((row_num, col_num), (row_num, i)))
                if row_num != i:
                    constraints.add(((row_num, col_num), (i, col_num)))

    # Gets all of the blocks
    blocks = []
    for row in range(3):
        for col in range(3):
            cur_block = []
            for ver in range(3):
                for horiz in range(3):
                    cur_block.append((row * 3 + ver, col * 3 + horiz))
            blocks.append(cur_block)

    # Accounts for the block constraints
    for block in blocks:
        for square in block:
            for constraint_square in block:
                if square != constraint_square:
                    constraints.add((square, constraint_square))

    return Puzzle(board, constraints)


def main():
    puzzle = parse_input("input.txt")
    puzzle.print_board()


if __name__ == "__main__":
    main()
