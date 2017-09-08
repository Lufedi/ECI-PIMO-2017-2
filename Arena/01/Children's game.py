import sys
def re(l,b):
    for i in range(b):
        for j in range(i+1,b):
            if int(l[i]+l[j])<int(l[j]+l[i]):
                l[i],l[j]=l[j],l[i]
    r=""
    for x in l:
        r=r+x
    return r
def main():
    n=int(sys.stdin.readline().strip())
    while n>0:
        l=sys.stdin.readline().split()
        print(re(l,n))
        n=int(sys.stdin.readline().strip())
main()
