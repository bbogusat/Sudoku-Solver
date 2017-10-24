class Sudoku: 
    def __init__(self, textInput):
        file = open(textInput, "r")
        values = []
        for i in range(0, 9):
            line = file.readline().split(' ')
            values.append([])
            for j in range(0, 9): 
                values[i].append(int(line[j]))
            print()
        

Sudoku("input.txt")
    