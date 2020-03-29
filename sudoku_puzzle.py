import itertools

class sudoku_puzzle:
    
    def __init__(self, puzzle = None):
        if (puzzle):
            self.puzzle = puzzle
        else:
            self.puzzle = sudoku_puzzle.gen_puzzle()
        self.x_pos = 0
        self.y_pos = 0

    @staticmethod
    def gen_puzzle():
        return [
            [0,2,0,3,4,0,0,0,1],
            [8,5,0,0,2,0,0,4,0],
            [0,0,3,0,0,1,2,5,6],
            [0,0,0,0,3,0,7,6,0],
            [0,0,4,1,6,0,5,9,0],
            [6,8,0,4,0,0,0,0,0],
            [5,0,8,0,0,3,0,0,0],
            [1,9,7,2,5,4,0,0,0],
            [0,4,2,0,0,7,9,1,0]
        ]

    def assign_number(self, x_pos, y_pos, number):
        self.puzzle[y_pos][x_pos] = number
    
    def print_puzzle(self):
        for row in self.puzzle:
            print(row)

    def get_row(self, row_number):
        return self.puzzle[row_number]

    def get_column(self, column_number):
        return [row[column_number] for row in self.puzzle]

    def get_square(self, x_pos, y_pos):
        square_x_pos = x_pos // 3
        square_y_pos = y_pos // 3
        square = []
        for i in range(3):
            square.append(self.puzzle[square_y_pos * 3 + i][square_x_pos * 3 : square_x_pos * 3 + 3])
        return square



    def check_if_number(self, x_pos, y_pos, number):
        row_check = number in self.get_row(y_pos)
        column_check = number in self.get_column(x_pos)
        square_check = number in [i for arr in self.get_square(x_pos,y_pos) for i in arr]
        if (row_check or column_check or square_check):
            return False
        return True

    def get_next_open_slot(self, x_pos, y_pos):
        for x in range(x_pos, 9):
            if (self.puzzle[y_pos][x] == 0):
                return {"x": x, "y": y_pos}
        for y in range(y_pos + 1, 9):
            for x in range(0, 9):
                if (self.puzzle[y][x] == 0):
                    return {"x": x, "y": y}
        return None



if __name__ == "__main__":
    puzzle = sudoku_puzzle()
    puzzle.print_puzzle()