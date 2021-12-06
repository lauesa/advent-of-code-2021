import numpy as np
import copy

class Board(object):
    def __init__(self, board):
        self.board = np.matrix(board)
        self.rboard = np.rot90(self.board).tolist()
        self.board = self.board.tolist()
        self.won = False
    
    def draw(self):
        print np.matrix(self.board)

    def score(self, guessed):
        d = [int(item) for elem in self.board for item in elem if item not in guessed]
        unmarked = sum(d)
        multi = int(guessed[-1])

        if not self.won:
            self.draw()
            self.won = True
            print multi * unmarked

    def is_winner(self, guessed):
        guess = set(guessed)
        for row in self.board:
            if(set(row).issubset(guess)):
                self.score(guessed)
                return True
        for row in self.rboard:
            if(set(row).issubset(guess)):
                self.score(guessed)
                return True
        return False


boards = []
with open("input.txt") as file:
    for i, line in enumerate(file):
        if i == 0:
            call = np.asarray(line.strip().split(','))
        if line == "\n":
            # generate board object
            bl = []
            for _ in range(5):
                row = np.asarray(file.next().strip().split())
                bl.append(row)
            obj = Board(np.array(bl))
            boards.append(obj)

called = []
done = False
for b in call:
    called.append(b)
    for board in boards:
        board.is_winner(called)

