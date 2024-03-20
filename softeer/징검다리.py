import sys
from bisect import bisect_left

input = sys.stdin.readline
N = input()
A = tuple(map(int, input().split()))

temp = [A[0]]
for i in range(1, len(A)):
    if temp[-1] < A[i]:
        temp.append(A[i])
    else:
        temp[bisect_left(temp, A[i])] = A[i]

print(len(temp))
