class Sudoku: 
    values = []
    def __init__(self, textInput):
        file = open(textInput, "r")
        for i in range(0, 9):
            line = file.readline().split(' ')
            self.values.append([])
            for j in range(0, 9):             
                self.values[i].append(cspSquare(int(line[j])))
                
    def printSudoku(self):
        for i in self.values: 
            for j in i: 
                print(j.value, end = ' ')
            print()
            
    def columnConstraint(self, row, column):
        columnPopArray = []
        for i in self.values: 
            if (i[column].value != 0): 
                columnPopArray.append(i[column].value)
        
        self.values[row][column].popDomain(columnPopArray)
        
        
    def rowConstraint(self, row, column):
        rowPopArray = []
        for i in self.values[row]: 
            if (i.value != 0): 
                rowPopArray.append(i.value)
         
        self.values[row][column].popDomain(rowPopArray)
        
        
    def boxConstraint(self, row, column):
        boxPopArray= []
        for i in range(3*(row//3),(3*(row//3))+3):
            for j in range(3*(column//3),(3*(column//3))+3):
                if (self.values[i][j].value != 0): 
                    boxPopArray.append(self.values[i][j].value)
        
        self.values[row][column].popDomain(boxPopArray)
                

class cspSquare: 
    domain = [1,2,3,4,5,6,7,8,9]
    value = 0
    def __init__(self, value):
        if (value != 0):
            self.domain = []
            self.value = value
        
    def popDomain(self, values):
        for i in values: 
            if i in self.domain: 
                self.domain.remove(i)
                
        if (len(self.domain) == 1): 
            self.value = self.domain[0]
    

s = Sudoku("input.txt")
s.printSudoku()






    