



INF = 9999999999999999999

numbers = [1,2, 4,9,8,7,12,21,34,1,0,11,4,-9,3,54,21,1]

maximun = -1*INF
minimun = INF


for a in  numbers:
    if(a >= maximun): maximun = a
    if(a <= minimun): minimun = a

print("The highest difference is: ", maximun-minimun)



diff = -1*INF

for a in numbers:
    for b in numbers:
        if(a - b > diff):  diff = a - b

print("The highest difference is: ", diff)



#Binary search

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        pos = 0
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            pos = midpoint
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return (pos, found)


