from sys import stdin

def main():
    line =  stdin.readline().strip()
    while line != "0 0":
        R = int(line[0])
        C = int(line[0])
        mat = [ 0 for i in range(C)]
        for i in range(R):
            line = stdin.readline()
            for j in range(C):
                if(line[j] == '#'):
                    mat[i][j] = 0
                elif(line[j] == '.'):
                    mat[i][j] = 1
                elif (line[j] == 'B'):
                    mat[i][j] = 2
                elif (line[j] == 'b'):
                    mat[i][j] = 3
                elif (line[j] == 'W'):
                    mat[i][j] = 4
                elif (line[j] == 'w'):
                    mat[i][j] = 5
        instructions =  stdin.readline().strip()





