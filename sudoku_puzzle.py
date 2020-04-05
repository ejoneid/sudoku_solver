import itertools
import sys

sys.setrecursionlimit(1000000)

empty_puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

example_puzzle = [
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
        print("")
        for row in self.puzzle:
            print(row)


    def get_row(self, y_pos):
        return self.puzzle[y_pos]


    def get_column(self, x_pos):
        return [row[x_pos] for row in self.puzzle]


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


    def get_possible_numbers(self, x_pos, y_pos):
        pos_numbers = [i for i in range(1,10)]
        row = self.get_row(y_pos)
        col = self.get_column(x_pos)
        square = [i for arr in self.get_square(x_pos,y_pos) for i in arr]
        for num in range(1,10):
            if num in (row + col + square):
                pos_numbers.remove(num)
        return pos_numbers


    def get_next_open_slot(self, x_pos, y_pos):
        for x in range(x_pos, 9):
            if (self.puzzle[y_pos][x] == 0):
                return {"x": x, "y": y_pos}
        for y in range(y_pos + 1, 9):
            for x in range(0, 9):
                if (self.puzzle[y][x] == 0):
                    return {"x": x, "y": y}
        return None


    def is_solved(self):
        for row in self.puzzle:
            if 0 in row:
                return False
        return True
    

    def solve_with_backtracking(self):

        moves = []
        def move_and_place(self, x_pos, y_pos, atempt_nr):
            self.assign_number(x_pos, y_pos, 0)
            if (atempt_nr >= len(self.get_possible_numbers(x_pos, y_pos))):
                move = moves.pop()
                move_and_place(self, move["x"], move["y"], move["atempts"])
            else:
                num_to_try = self.get_possible_numbers(x_pos, y_pos)[atempt_nr]
                self.assign_number(x_pos, y_pos, num_to_try)
                moves.append({"x": x_pos, "y": y_pos, "atempts": atempt_nr + 1})

                next_move = self.get_next_open_slot(x_pos, y_pos)
                if (not next_move):
                    return
                
                possibilities_on_next_move = self.get_possible_numbers(next_move["x"], next_move["y"])
                if (possibilities_on_next_move):
                    move_and_place(self, next_move["x"], next_move["y"], 0)
                else:
                    move = moves.pop()
                    move_and_place(self, move["x"], move["y"], move["atempts"])
        
        move_and_place(self, 0, 0, 0)


    # unfinished
    def solve(self):
        while (not self.is_solved()):
            x = 0
            y = 0
            while (self.get_next_open_slot(x, y)):
                x_pos = self.get_next_open_slot(x, y)["x"]
                y_pos = self.get_next_open_slot(x, y)["y"]

                pos_num = self.get_possible_numbers(x_pos, y_pos)
                if (len(pos_num) == 1):
                    puzzle.assign_number(x_pos, y_pos, pos_num[0])
                
                if (x == 8):
                    x = 0
                    y = y_pos + 1
                else:
                    x = x_pos + 1
                    y = y_pos



if __name__ == "__main__":
    puzzle = sudoku_puzzle(example_puzzle)
    puzzle.print_puzzle()
    puzzle.solve_with_backtracking()
    puzzle.print_puzzle()
    