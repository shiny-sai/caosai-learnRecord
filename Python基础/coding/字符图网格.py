"""
@FileName：字符图网格.py
@Description：
@Author：CaoSai
@Time：2022/11/22 19:34
"""


def print_grid(grid):
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                print(grid[y][x], end='')
            print()

_grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print_grid(_grid)
