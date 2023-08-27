import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
data = tuple(map(int, input().split()))

lis = [data[0]]
lidx = 0

i = 1
while i < N:
    if lis[-1] < data[i]:
        lis.append(data[i])
        lidx += 1
    else:
        lis[bisect_left(lis, data[i])] = data[i]

    i += 1

print(lidx + 1)