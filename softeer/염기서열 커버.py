import sys
input = sys.stdin.readline
from math import ceil

N, M = map(int, input().split())
bases = list()
for _ in range(N):
    bases.append(list(input().strip()))

data = [[] for _ in range(2 ** N)]
data[0] = '.' * M
for index in range(1, 2 ** N):
    temp = index
    loc = 0
    while temp % 2 == 0:
        temp //= 2
        loc += 1

    base1 = bases[loc]
    base2 = data[index - 2 ** loc]

    if base1 == [] or base2 == []:
        data[index] = []
        continue

    base = list()
    for i in range(M):
        if base1[i] == '.':
            base.append(base2[i])
        elif base2[i] == '.':
            base.append(base1[i])
        elif base1[i] == base2[i]:
            base.append(base1[i])
        else:
            base = list()
            break
    data[index] = base
            
answer = [N+1] * (2 ** N)
answer[0] = 0
for index in range(1, 2 ** N):
    if data[index] != []:
        answer[index] = 1
    else:
        temp = index
        bits = list()
        loc = 0
        while temp > 0:
            if temp % 2 == 1:
                bits.append(2 ** loc)
            loc += 1
            temp //= 2
    
        index1 = 0
        index2 = index
        b = len(bits)
        
        digit = [0] * b
        for i in range(1, 2 ** (b - 1)):
            for j in range(b):
                if digit[j] == 1:
                    digit[j] = 0
                    index1 -= bits[j]
                    index2 += bits[j]
                else:
                    digit[j] = 1
                    index1 += bits[j]
                    index2 -= bits[j]
                    break
            number = answer[index1] + answer[index2]
            if number < answer[index]:
                answer[index] = number

print(answer[-1])
