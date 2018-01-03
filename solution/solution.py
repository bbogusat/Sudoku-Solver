DEFAULT_DOMAIN = {1, 2, 3, 4, 5, 6, 7, 8, 9}


class Square:
    def __init__(self, domain):
        self.domain = domain
        self.neighbours = set()

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

    def popDomain(self, value):
        self.domain = self.domain.difference(value)

    def getDomain(self):
        return self.domain

    def GetNeighbours(self):
        return self.neighbours


class Puzzle:
    def __init__(self, board, constraints):
        # list of squares
        self.board = board
        # List of constraints. Assumed to be != in the form of board coordinates
        # Using index as the Hash of the Square in the set will change with update of domain
        # ((Row, Col), (Row,Col))
        self.constraints = constraints

    def __repr__(self):
        shows = "Squares: " + str(self.board) + \
            "\nConstraints:" + str(self.constraints)
        return shows

    def solve_ac3(self):
        print("Solving . . . \n")
        while(len(self.constraints) != 0):
            row_col_values = self.constraints.pop()
            constraint = []
            for val in row_col_values:
                row = val[0]
                col = val[1]
                constraint.append(self.board[row][col])
            # if constraint 1 value is in the domain of constraint 0,
            # remove that value from constraint 0 domain

            if (len(constraint[1].getDomain()) == 1 and
                    (constraint[0].getDomain().issuperset(constraint[1].getDomain()))):
                constraint[0].popDomain(constraint[1].getDomain())
                if len(constraint[0].getDomain()) == 0:
                    print("There are no more possible values for the: " +
                          str(row_col_values[0]) + " square!")
                    print("Arc-consistent CSP cannot be found.")
                    return False

                self.constraints.update(constraint[0].GetNeighbours())
        print("Arc-Consistent version found")

        return True

    def print_board(self):
        print("Sudoku Puzzle:")
        for r_num in range(len(self.board)):
            if r_num != 0:
                print()
            for c_num in range(len(self.board)):
                square = self.board[r_num][c_num]
                cur_domain = square.getDomain()
                if c_num != 0:
                    print(" ", end="")
                if len(cur_domain) != 1:
                    print('0', end="")
                else:
                    for val in cur_domain:
                        print(val, end="")
                if c_num % 3 == 2:
                    if c_num != len(self.board) - 1:
                        print(" |", end="")
                    elif r_num % 3 == 2 and r_num != len(self.board) - 1:
                        print("\n------+-------+------", end="")
        print("\n")


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
            if int(line[j]) == 0:
                board[i].append(Square(DEFAULT_DOMAIN))
            else:
                board[i].append(Square({int(line[j])}))

    # Constraint is assumed to be !=
    constraints = set()

    # Accounts for the row and column constraints
    board_size = len(board)
    for row_num in range(board_size):
        for col_num in range(board_size):
            for i in range(board_size):
                if col_num != i:
                    board[row_num][col_num].GetNeighbours().add(
                        ((row_num, i), (row_num, col_num)))
                    constraints.add(((row_num, col_num), (row_num, i)))
                if row_num != i:
                    board[row_num][col_num].GetNeighbours().add(
                        ((i, col_num), (row_num, col_num)))
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
                    board[square[0]][square[1]].GetNeighbours().add((constraint_square,
                                                                     square))
                    constraints.add((square, constraint_square))

    return Puzzle(board, constraints)


def main():
    puzzle = parse_input("input.txt")
    puzzle.print_board()
    if(puzzle.solve_ac3()):
        puzzle.print_board()


if __name__ == "__main__":
    main()
