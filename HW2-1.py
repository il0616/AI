def queen(index):
    for k in range(0, n):
        col[index] = k
        if promising(index):
            if n == index + 1 or queen(index + 1):
                return True

    return False

def promising(index):
    for k in range(0, index):
        if col[index] == col[k] or abs(col[index] - col[k]) == abs(index - k):
            return False
    return True


fileName = input("[n-Queen] input file name? : ")
inputFile = open(fileName, 'r')
n = int(inputFile.read())
col = [0] * n

import random

ceiling = int(n*39 / 40)
while True:
    for i in range(0, ceiling):
        col[i] = random.randrange(0, n)
        j = 0
        while j < ceiling:
            col[i] = random.randrange(0, n)
            j += 1
            if promising(i):
                break
        else:
            break
    else:
        if queen(ceiling):
            break

for i in range(len(col)):
    col[i] += 1
print(col)

outputFile = open("output.txt", 'w')
for val in col:
    outputFile.write("%d\n" % val)