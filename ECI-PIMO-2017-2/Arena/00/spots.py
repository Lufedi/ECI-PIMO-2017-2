from sys import stdin

taken = []
for i in range(505):
    a = []
    for j in range(505):
        a.append([])
    taken.append(a)




def main():

    W = 0
    H = 0
    N = 0
    print("sss")
    line = stdin.readline().strip()
    data = line.split(" ")
    print(data)
    W = int(data[0])
    H = int(data[1])
    N = int(data[2])
    while ( W != 0 and H !=0 and N != 0):
        print(data)
        for i in range(N):
            X1 = 0
            X2 = 0
            Y1 = 0
            Y2 = 0
            data = stdin.readline().strip().split(" ")
            print(data)
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


            for y in range(Y1 - 1 , Y2):
                for x  in range( X1 - 1, X2):
                    taken[y][x] =  True

        count = 0
        for y in range( H):
            for x in range(W):
                if (not taken[y][x]):
                    count+=1
                else:
                    taken[y][x] = False

        if (count == 0):
            print("There is no empty spots.")
        elif (count == 1):
            print("There is one empty spot.")
        else:
            print("There are %d empty spots." % count)
        stdin.readline()
        #line = stdin.readline().strip()
        data = line.split(" ")
        W = int(data[0])
        H = int(data[1])
        N = int(data[2])

main()