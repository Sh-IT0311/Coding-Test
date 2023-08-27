import sys
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())

teams = defaultdict(list)
for _ in range(N):
    x,y,k = map(int, input().split())
    teams[k].append((x,y))

answer = float('inf')
def dfs(now, x_min, x_max, y_min, y_max):
    global answer
    if now > K:
        answer = min((x_max - x_min) * (y_max - y_min), answer)
        return

    if answer <= (x_max - x_min) * (y_max - y_min):
        return

    for x,y in teams[now]:
        xmax = max(x, x_max)
        xmin = min(x, x_min)

        ymin = min(y, y_min)
        ymax = max(y, y_max)

        dfs(now+1, xmin,xmax,ymin,ymax)

for x,y in teams[1]:
    dfs(1,x,x,y,y)

print(answer)