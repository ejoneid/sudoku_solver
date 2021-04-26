# sudoku_solver
This is a sudoku solver for 9x9 puzzles.

## Usage
```python
from sudoku_solver import sudoku_solver

examplePuzzle = [
    [5, 8, 6, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 6, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [9, 0, 2, 0, 1, 0, 3, 0, 5],
    [0, 0, 5, 0, 9, 0, 0, 0, 0],
    [0, 9, 0, 0, 4, 0, 0, 0, 8],
    [0, 0, 3, 5, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 2, 0, 4, 7, 0]
]

puzzleObject = sudoku_puzzle(puzzle=examplePuzzle)
puzzleObject.solve()
```
