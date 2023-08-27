import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
answer = 1

lcnt = [1]
lflag = [True]

lis = [arr[0]]
j = 0

i = 1
while i < n:
    flag = False
    if lis[j] < arr[i]:
        lis.append(arr[i])
        j += 1
        flag = True

    else:
        lis[bisect_left(lis, arr[i])] = arr[i]

    lcnt.append(j+1)
    lflag.append(flag)
    i += 1


lis = [arr[n-1]]
j = 0

i = n-2
while i >= 0:
    flag = False
    if lis[j] < arr[i]:
        lis.append(arr[i])
        j += 1
        flag = True

    else:
        lis[bisect_left(lis, arr[i])] = arr[i]

    answer = max(answer, lcnt[i] + j + 1 - int(lflag[i] and flag))
    i -= 1

print(answer)