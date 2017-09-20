




from collections import deque


def parChecker(symbolString):
    s = []
    balanced = True
    index = 0
    for i in range(len(symbolString)):
        symbol = symbolString[i]
        if symbol == "(":
            s.append(symbol)
        else:
            if len(s) ==0:
                balanced = False
            else:
                s.pop()


    if balanced and len(s) ==0:
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('(()'))



from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
print("1",queue)
queue.append("Graham")          # Graham arrives
print("2",queue)
queue.popleft()                 # The first to arrive now leaves
print("3",queue)
queue.popleft()                 # The second to arrive now leaves
print("4",queue)
queue.append("Fernand")          # Graham arrives
print("5",queue)                    # Remaining queue in order of arrival



def hotPotato(namelist, num):
    simqueue = deque()
    for name in namelist:
        simqueue.append(name)

    while len(simqueue) > 1:
        for i in range(num):
            simqueue.append(simqueue.popleft())
        simqueue.popleft()

    return simqueue.popleft()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))




from collections import  deque

def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.append(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop()
        last = chardeque.popleft()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
