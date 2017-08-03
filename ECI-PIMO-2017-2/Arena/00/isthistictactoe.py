import time
from sys import stdin

from multiprocessing.pool import Pool
parallelSolve = False
INF = 1 << 30


def solve(par):
    def checkwin():
        if countO == 3:
            win[0] = True
        if countX == 3:
            win[1] = True

    board = par
    totalO = totalX = 0  # first one is O, second is X
    win = [False, False]

    for i in range(3):
        countO = countX = 0
        for j in range(3):
            if board[i][j] == 'O':
                countO += 1
            elif board[i][j] == 'X':
                countX += 1
        totalO += countO
        totalX += countX
        checkwin()

    for j in range(3):
        countO = countX = 0
        for i in range(3):
            if board[i][j] == 'O':
                countO += 1
            elif board[i][j] == 'X':
                countX += 1
        checkwin()

    countO = countX = 0
    for i in range(3):
        if board[i][i] == 'O':
            countO += 1
        elif board[i][i] == 'X':
            countX += 1
        checkwin()

    countO = countX = 0
    for i in range(3):
        if board[i][2 - i] == 'O':
            countO += 1
        elif board[i][2 - i] == 'X':
            countX += 1
        checkwin()

    if totalO > totalX or totalX > totalO + 1:
        return False
    if win[0] and win[1]:
        return False
    if win[0] and totalO < totalX:
        return False
    if win[1] and totalX <= totalO:
        return False
    return True


class Solver:



    def __init__(self):
        self.results = []



    def solve(self):


        self.numOfTests = int(stdin.readline().strip())
        self.input = []
        for i in range(self.numOfTests):
            board = []
            for j in range(3):
                board.append(stdin.readline().strip())
            self.input.append(list(board))
            stdin.readline().strip()

        for i in self.input:
            print(i)
            self.results.append(solve(i))

        for test in range(self.numOfTests):
            print("Case #%d: %s\n" % (test + 1, self.results[test]))




if __name__ == '__main__':
    solver = Solver()
    solver.solve()