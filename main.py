from random import randint


class MineField:
    def __init__(self, size, n_bombs):
        self.size = size
        self.n_bombs = n_bombs
        self.grid = [[None for j in range(size)] for i in range(size)]
        self.plant_bombs()
        self.assign_numbers()
        
    def __str__(self):
        _str = ''
        for row in self.grid:
            for char in row:
                _str += str(char) + ' '
            _str += '\n'
        return _str
        
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.n_bombs:
            row = randint(0, self.size - 1)
            column = randint(0, self.size - 1)
            
            if self.grid[row][column] == '*':
                continue
            
            self.grid[row][column] = '*'
            bombs_planted += 1
            
    def assign_numbers(self):
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == '*':
                    continue
                
                neighbor_bombs = 0
                
                if row != 0:
                    if column != 0:
                        if self.grid[row-1][column-1] == '*':
                            neighbor_bombs += 1
                            
                    if self.grid[row-1][column] == '*':
                        neighbor_bombs += 1
                        
                    if column != self.size-1:
                        if self.grid[row-1][column+1] == '*':
                            neighbor_bombs += 1
                            
                if column != 0:
                    if self.grid[row][column-1] == '*':
                        neighbor_bombs += 1
                if column != self.size-1:
                    if self.grid[row][column+1] == '*':
                        neighbor_bombs += 1
                        
                if row != self.size-1:
                    if column != 0:
                        if self.grid[row+1][column-1] == '*':
                            neighbor_bombs += 1
                            
                    if self.grid[row+1][column] == '*':
                        neighbor_bombs += 1
                        
                    if column != self.size-1:
                        if self.grid[row+1][column+1] == '*':
                            neighbor_bombs += 1
                            
                self.grid[row][column] = neighbor_bombs
        
        
hola = MineField(5, 10);
print(hola)
print(hola.grid)
