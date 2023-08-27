import sys
from collections import deque
input = sys.stdin.readline

H, K, R = map(int, input().split())

leaves = dict()
temp = 2 ** H
for i in range(temp):
    leaves[temp + i] = deque(map(int, input().split()))

left = [deque() for _ in range(temp)]
right = [deque() for _ in range(temp)]

for days in range(1, R+1):
    if days % 2 == 0: # even
        data = right
    else: # add
        data = left
    
    for i in range(1, 2 ** (H+1)):
        upper, flag = divmod(i, 2)
        
        if flag:
            target = right
        else:
            target = left
        
        if i < temp:
            if data[i]:
                target[upper].append(data[i].popleft())
        else:
            if leaves[i]:
                target[upper].append(leaves[i].popleft())

print(sum(right[0]))
