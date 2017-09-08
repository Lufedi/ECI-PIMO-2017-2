from sys import stdin

def main():

    W = 0
    H = 0
    N = 0

    line = stdin.readline().strip()
    data = line.split(" ")

    W = int(data[0])
    H = int(data[1])
    N = int(data[2])
    while ( W != 0 or H != 0 or N != 0):

        taken = []
        for i in range(505):
            taken.append([False for j in range(505)])


        for i in range(N):
            X1 = 0
            X2 = 0
            Y1 = 0
            Y2 = 0
            data = stdin.readline().strip().split(" ")

            X1 = int(data[0])
            Y1 = int(data[1])
            X2 = int(data[2])
            Y2 = int(data[3])

            if( X1 > X2):
                c = X2
                X2 = X1
                X1 = c

            if( Y1 > Y2):
                c = Y2
                Y2 = Y1
                Y1 =  c


            for x in range(X1 - 1 , X2):
                for y  in range( Y1 - 1, Y2):
                    taken[x][y] =  True


        count = 0
        for x in range(W):
            for y in range(H):
                if (taken[x][y] == True):
                    taken[x][y] = True
                else:
                    count += 1

        if (count == 0):
            print("There is no empty spots.")
        elif (count == 1):
            print("There is one empty spot.")
        else:
            print("There are %d empty spots." % count)
        stdin.readline()

        data = stdin.readline().split(" ")
        W = int(data[0])
        H = int(data[1])
        N = int(data[2])


main()