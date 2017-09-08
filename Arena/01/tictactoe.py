
import time
from sys import stdin

def HasNotWon(grid ,character):

    if (grid[0][0] == character and grid[0][1] == character and grid[0][2] == character):
        return False

    if (grid[1][0] == character and grid[1][1] == character and grid[1][2] == character):
        return False

    if (grid[2][0] == character and grid[2][1] == character and grid[2][2] == character):
        return False

    if (grid[0][0] == character and grid[1][0] == character and grid[2][0] == character):
        return False

    if (grid[0][1] == character and grid[1][1] == character and grid[2][1] == character):
        return False

    if (grid[0][2] == character and grid[1][2] == character and grid[2][2] == character):
        return False

    if (grid[0][0] == character and grid[1][1] == character and grid[2][2] == character):
        return False

    if (grid[0][2] == character and grid[1][1] == character and grid[2][0] == character):
        return False

    return True


def main():
    t = int(stdin.readline().strip())

    for k in range(t):
        g = []
        xCount  = 0
        oCount = 0
        for i in range(3):
            g.append(stdin.readline().strip())
            for j in range(3):
                if g[i][j] == 'X':
                    xCount += 1
                elif g[i][j] == 'O':
                    oCount += 1

        if (xCount == oCount):
            valid = HasNotWon(g, 'X') elif(xCount == (oCount + 1)):
            valid = HasNotWon(g, 'O')
        else:
            valid = False

        if (valid):
            print("yes")
        else:
            print("no")
        if(k != t- 1): stdin .readline()

main()