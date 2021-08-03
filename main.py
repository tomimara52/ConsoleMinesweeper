from random import randint, choice
import os
import re
from time import sleep


class MineField:
    def __init__(self, size, n_bombs):
        self.size = size
        self.n_bombs = n_bombs
        self.grid = [[None for j in range(size)] for i in range(size)]
        self.grid_mask = [['·' for j in range(size)] for i in range(size)]
        self.plant_bombs()
        self.assign_numbers()
        self.first_dig()
        
    def __str__(self):
            
        _str = '    ';
        
        for i in range(1, self.size+1):
            _str += str(i) + ' '
            if i < 10:
                _str += ' '
        _str += '\n'
        
        _str += ' ' + '―' * (self.size * 3 + 3) + '\n'
        
        for i, row in enumerate(self.grid_mask, 1):
            if i < 10:
                _str += ' '
            _str += str(i) + '| '
            for char in row:
                _str += str(char) + '  '
            _str += '\n'
        return _str
    
    def __strraw__(self):
            
        _str = '    ';
        
        for i in range(1, self.size+1):
            _str += str(i) + ' '
            if i < 10:
                _str += ' '
        _str += '\n'
        
        _str += ' ' + '―' * (self.size * 3 + 3) + '\n'
        
        for i, row in enumerate(self.grid, 1):
            if i < 10:
                _str += ' '
            _str += str(i) + '| '
            for char in row:
                _str += str(char) + '  '
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
                
    def first_dig(self):
        zeros = []
        for row in range(self.size):
            for column in range(self.size):
                if self.grid[row][column] == 0:
                    zeros.append((row, column))
                    
        spot_to_dig = choice(zeros)
        self.dig(spot_to_dig[0], spot_to_dig[1])
        
    def dig(self, row, col):
        spot = self.grid[row][col]
        if spot == '*':
            lose()
        elif spot != self.grid_mask[row][col]:
            self.grid_mask[row][col] = spot
            if (spot == 0):
                self.clear_zeros(row, col)
            
    def clear_zeros(self, row, col):
        if row != 0:
            if col != 0:
                if self.grid[row-1][col-1] != '*':
                    self.dig(row-1, col-1)
                    
            if self.grid[row-1][col] != '*':
                self.dig(row-1, col)
                
            if col != self.size-1:
                if self.grid[row-1][col+1] != '*':
                    self.dig(row-1, col+1)
                    
        if col != 0:
            if self.grid[row][col-1] != '*':
                self.dig(row, col-1)
        if col != self.size-1:
            if self.grid[row][col+1] != '*':
                self.dig(row, col+1)
                
        if row != self.size-1:
            if col != 0:
                if self.grid[row+1][col-1] != '*':
                    self.dig(row+1, col-1)
                    
            if self.grid[row+1][col] != '*':
                self.dig(row+1, col)
                
            if col != self.size-1:
                if self.grid[row+1][col+1] != '*':
                    self.dig(row+1, col+1)
            

def print_help():
    print('――――― Console Minesweeper ―――――')
    print('To dig in a spot, input the row\nand the column you want to dig in.')
    print('For example, if I wanted to dig\nin the row 2, column 4, I would\ntype: 2,4')
    print('―――――――――――――――――――――――――――――――――')
    print('If you just want to mark a spot\nwhere you know is a bomb, type the\ncoordinates followed with an "m".\nExample: 1,4m')
    print('\n')
    

def play(field):        
    os.system('cls' if os.name == 'nt' else 'clear')
    move = 'h'
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(field)
        # print(field.__strraw__())

        pattern = re.compile(r"^[0-9]+,[0-9]+m?$")
        
        
        if move == 'h':
            print_help()
        elif move == 'q':
            print('Bye!')
            break
        elif re.fullmatch(pattern, move):
                row, column= [int(i) for i in move.strip('m').split(',')]
                if (row > field.size) |( column > field.size):
                    print('Invalid coordinates')
                else:
                    print('Valid coordinates')
        else:
            print('Invalid input')
        
        move = input("Your move ('h' for help, 'q' to quit): ")
        
hola = MineField(8, 10)
play(hola)
