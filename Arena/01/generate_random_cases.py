import random
for i in range(100):
    line = ""
    for i in range(random.randint(3, 16)):
        n = random.randint(1, 1000)
        if(i == 0):
            line += str(n)
        else: line+= " "+ str(n)
    print(line)
print("0")
