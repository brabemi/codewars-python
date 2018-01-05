import math
from collections import namedtuple

from pprint import pprint

CellId = namedtuple('CellId', ['row', 'col'])
Cell = namedtuple('Cell', ['val', 'pos_vals', 'collide'])

def get_colliders(row, col, size, block_size):
    colliders = set()
    for i in range(size):
        if i != row:
            colliders.add(CellId(row=i, col=col))
        if i != col:
            colliders.add(CellId(row=row, col=i))
    b_row = row - row % block_size
    b_col = col - col % block_size
    for i in range(size):
        tmp_row = b_row + i // block_size
        tmp_col = b_col + i % block_size
        if row != tmp_row or col != tmp_col:
            colliders.add(CellId(row=tmp_row, col=tmp_col))
    return colliders

def remove_collision(sudoku, cell):
    for collision in cell.collide:
        sudoku[collision].pos_vals.discard(cell.val)

def init_sudoku(puzzle):
    sudoku = {}
    size = len(puzzle)
    block_size = int(math.sqrt(size))
    unsolved = size**2
    for row in range(size):
        for col in range(size):
            sudoku[CellId(row=row, col=col)] = Cell(
                val=puzzle[row][col],
                pos_vals=set() if puzzle[row][col] != 0 else set(range(1,size+1)),
                collide=get_colliders(row, col, size, block_size)
            )
    for position, cell in sudoku.items():
        if cell.val != 0:
            unsolved -= 1
            remove_collision(sudoku, cell)
    return sudoku, unsolved

def sudoku(puzzle):
    sudoku, unsolved = init_sudoku(puzzle)
    clear = [pos for pos, cell in sudoku.items() if len(cell.pos_vals) == 1 ]
    while unsolved > 0 and len(clear) > 0:
        pos = clear.pop()
        sudoku[pos] = sudoku[pos]._replace(val=sudoku[pos].pos_vals.pop())
        remove_collision(sudoku, sudoku[pos])
        unsolved -= 1
        if len(clear) == 0:
            clear = [pos for pos, cell in sudoku.items() if len(cell.pos_vals) == 1 ]
    for pos, cell in sudoku.items():
        puzzle[pos.row][pos.col] = cell.val
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

solution = [[5,3,4,6,7,8,9,1,2],
            [6,7,2,1,9,5,3,4,8],
            [1,9,8,3,4,2,5,6,7],
            [8,5,9,7,6,1,4,2,3],
            [4,2,6,8,5,3,7,9,1],
            [7,1,3,9,2,4,8,5,6],
            [9,6,1,5,3,7,2,8,4],
            [2,8,7,4,1,9,6,3,5],
            [3,4,5,2,8,6,1,7,9]]

# print(sudoku(puzzle))
print(sudoku(puzzle), solution, "Incorrect solution for the following puzzle: " + str(puzzle))
