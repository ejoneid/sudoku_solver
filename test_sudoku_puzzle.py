import unittest
import sudoku_puzzle

class TestSudoku(unittest.TestCase):

    def setUp(self):
        testPuzzle = [
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
        self.puzzle = sudoku_puzzle.sudoku_puzzle(puzzle=testPuzzle)

    def test_assign_number(self):
        self.puzzle.assign_number(0,0,4)
        self.puzzle.assign_number(7,0,3)
        self.puzzle.assign_number(3,8,7)
        correct_state = [
            [4,2,0,3,4,0,0,3,1],
            [8,5,0,0,2,0,0,4,0],
            [0,0,3,0,0,1,2,5,6],
            [0,0,0,0,3,0,7,6,0],
            [0,0,4,1,6,0,5,9,0],
            [6,8,0,4,0,0,0,0,0],
            [5,0,8,0,0,3,0,0,0],
            [1,9,7,2,5,4,0,0,0],
            [0,4,2,7,0,7,9,1,0]
        ]
        self.assertEqual(self.puzzle.puzzle, correct_state)

    def test_get_row(self):
        row0 = [0,2,0,3,4,0,0,0,1]
        row3 = [0,0,0,0,3,0,7,6,0]
        row8 = [0,4,2,0,0,7,9,1,0]
        self.assertEqual(self.puzzle.get_row(0), row0)
        self.assertEqual(self.puzzle.get_row(3), row3)
        self.assertEqual(self.puzzle.get_row(8), row8)

    def test_get_column(self):
        col0 = [0,8,0,0,0,6,5,1,0]
        col5 = [0,0,1,0,0,0,3,4,7]
        col7 = [0,4,5,6,9,0,0,0,1]
        self.assertEqual(self.puzzle.get_column(0), col0)
        self.assertEqual(self.puzzle.get_column(5), col5)
        self.assertEqual(self.puzzle.get_column(7), col7)

    def test_get_square(self):
        square1 = [[0, 2, 0], [8, 5, 0], [0, 0, 3]]
        square2 = [[3, 4, 0], [0, 2, 0], [0, 0, 1]]
        square3 = [[0, 0, 1], [0, 4, 0], [2, 5, 6]]
        square5 = [[0, 3, 0], [1, 6, 0], [4, 0, 0]]
        square6 = [[7, 6, 0], [5, 9, 0], [0, 0, 0]]
        square9 = [[0, 0, 0], [0, 0, 0], [9, 1, 0]]
        self.assertEqual(self.puzzle.get_square(1,1), square1)
        self.assertEqual(self.puzzle.get_square(3,2), square2)
        self.assertEqual(self.puzzle.get_square(6,1), square3)
        self.assertEqual(self.puzzle.get_square(3,3), square5)
        self.assertEqual(self.puzzle.get_square(6,3), square6)
        self.assertEqual(self.puzzle.get_square(8,8), square9)

    def test_check_if_number(self):
        self.assertFalse(self.puzzle.check_if_number(2,0,2))
        self.assertFalse(self.puzzle.check_if_number(0,0,5))
        self.assertTrue(self.puzzle.check_if_number(0,0,7))
        self.assertTrue(self.puzzle.check_if_number(6,1,3))

    def test_get_next_open_slot(self):
        res1 = {'x': 0, 'y': 0}
        res2 = {'x': 2, 'y': 0}
        res3 = {'x': 5, 'y': 0}
        res4 = {'x': 2, 'y': 1}
        res5 = {'x': 0, 'y': 3}
        res6 = {'x': 8, 'y': 8}
        self.assertEqual(self.puzzle.get_next_open_slot(0,0), res1)
        self.assertEqual(self.puzzle.get_next_open_slot(1,0), res2)
        self.assertEqual(self.puzzle.get_next_open_slot(3,0), res3)
        self.assertEqual(self.puzzle.get_next_open_slot(8,0), res4)
        self.assertEqual(self.puzzle.get_next_open_slot(8,2), res5)
        self.assertEqual(self.puzzle.get_next_open_slot(8,8), res6)

if __name__ == "__main__":
    unittest.main()