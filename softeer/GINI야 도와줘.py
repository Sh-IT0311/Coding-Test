import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
_map = list()
for _ in range(R):
    _map.append(list(input().rstrip()))

def solution(_map):
    time_flag = 1
    rains = deque()
    for i in range(R):
        for j in range(C):
            if _map[i][j] == 'W':
                sx, sy = i, j

            elif _map[i][j] == 'H':
                ex, ey = i, j
            
            elif _map[i][j] == '*':
                rains.append((i,j))
    
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    conditions = {'X', '*'}
    rconditions = {'X','*', 'H'}
    
    INF = 3001
    times = [[INF] * C for _ in range(R)]
    times[sx][sy] = 0
    
    q = deque([(0, sx, sy)])
    while q:
        time, x, y = q.popleft()

        if time_flag == time:
            time_flag += 1
            temp = deque()

            while rains:
                rx, ry = rains.popleft()

                for k in range(4):
                    rnx = rx + dx[k]
                    rny = ry + dy[k]

                    if rnx < 0 or rny < 0 or rnx >= R or rny >= C:
                        continue
                    
                    if _map[rnx][rny] not in rconditions:
                        temp.append((rnx, rny))
                        _map[rnx][rny] = '*'
            
            rains = temp

        if x == ex and y == ey:
            return times[ex][ey]

        if _map[x][y] == '*':
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if _map[nx][ny] not in conditions:
                cost = time + 1
                if cost < times[nx][ny]:
                    times[nx][ny] = cost
                    q.append((cost,nx,ny))

    return 'FAIL'

print(solution(_map))