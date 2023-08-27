# import sys
from collections import deque

# input = sys.stdin.readline

dr = [-1,0,1,0]
dc = [0,1,0,-1]


n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
q = deque([(r, c, d)])
while q:
    r, c, d = q.popleft()
    
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1
    
    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if graph[nr][nc] == 0:
            q.append((nr, nc, nd))
            break ##
        d = nd
    else:
        nd = (d + 2) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        if graph[nr][nc] == 1:
            break
        else:
            q.append((nr, nc, d))
    
print(cnt)