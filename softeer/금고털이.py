import sys
from heapq import heappop, heappush

input = sys.stdin.readline

W,N = map(int, input().split())
data = list()
for _ in range(N):
    m,p = map(int, input().split())
    heappush(data, (-p, m))

answer = 0
while data:
    if W <= 0:
        break

    p, m = heappop(data)
    p = -p

    temp = min(m, W)
    answer += p * temp
    W -= temp

print(answer)