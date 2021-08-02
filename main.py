from random import randint


class MineField:
    def __init__(self, size, n_bombs):
        self.size = size
        self.n_bombs = n_bombs
        self.grid = [[None for j in range(size)] for i in range(size)]
        self.plant_bombs()
        
    def plant_bombs(self):
        bombs_planted = 0
        while bombs_planted < self.n_bombs:
            row = randint(0, self.size - 1)
            column = randint(0, self.size - 1)
            
            if self.grid[row][column] == '*':
                continue
            
            self.grid[row][column] = '*'
            bombs_planted += 1

        
hola = MineField(5, 10);
