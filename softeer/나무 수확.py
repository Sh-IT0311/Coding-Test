import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
matrix = list()
for _ in range(n):
    matrix.append(list(map(int, input().split())))

max_values = [[0] * n for _ in range(n)]
max_values[n-1][n-1] = matrix[n-1][n-1]
rx = (-1, 0)
ry = (0, -1)
rq = deque([(matrix[n-1][n-1], n-1, n-1)])
while rq:
    value, x, y = rq.popleft()

    if value < max_values[x][y]:
        continue

    for k in range(2):
        nx = x + rx[k]
        ny = y + ry[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        temp = max(value, matrix[nx][ny])
        if max_values[nx][ny] < temp:
            max_values[nx][ny]= temp
            rq.append((temp, nx, ny))

distance = [[0] * n for _ in range(n)]
distance[0][0] = matrix[0][0] + max_values[0][0]
q = deque([(distance[0][0], matrix[0][0], max_values[0][0], 0, 0)])

dx = (0, 1)
dy = (1, 0)

while q:
    values, max_value, gap, x, y = q.popleft()

    if values < distance[x][y]:
        continue

    values -= gap
    
    for k in range(2):
        nx = x + dx[k]
        ny = y + dy[k]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        temp_value = max(max_value, matrix[nx][ny])
        temp_gap = max(temp_value, max_values[nx][ny])
        
        total = values + matrix[nx][ny] + temp_gap

        if distance[nx][ny] < total:
            distance[nx][ny] = total            
            q.append((total, temp_value, temp_gap, nx, ny))

print(distance[-1][-1])