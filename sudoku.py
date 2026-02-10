# pylint: disable=missing-docstring


def sudoku_validator(grid):
     for row in grid:
         if len(row) !=9:
             return False
     for i in range(9):
        row = set()
        column = set()
        for j in range(9):
            if grid[i][j] != '.':
                if grid[i][j] in row:
                    return False
                row.add(grid[i][j])
            if grid[j][i] != '.':
                    if grid[j][i] in column:
                        return False
                    column.add(grid[j][i])
     for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = set()
            for i in range(3):
               for j in range(3):
                val = grid[box_row + i][box_col + j]
                if val != '.':
                    if val in box:
                        return False
                    box.add(val)

     return True
