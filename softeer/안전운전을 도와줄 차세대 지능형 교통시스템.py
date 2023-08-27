import sys
from collections import deque, defaultdict
input = sys.stdin.readline

dx = (-1,0,1,0)
dy = (0,1,0,-1)

directions = [set()]
directions.append([1,0,2])
directions.append([0,3,1])
directions.append([3,0,2])
directions.append([2,3,1])
directions.append([1,0])
directions.append([0,3])
directions.append([3,2])
directions.append([2,1])
directions.append([1,2])
directions.append([0,1])
directions.append([3,0])
directions.append([2,3])

N, T = map(int, input().split())
crosses = [[] for _ in range(N)]

for i in range(N):
    for _ in range(N):
        crosses[i].append(tuple(map(int, input().split())))

q = deque()
visited = [[False] * N for _ in range(N)]
#overlap = [[[[False] * 4 for _ in range(4)] for _ in range(N)] for _ in range(N)]
overlap = [[defaultdict(lambda : defaultdict(lambda : False)) for _ in range(N)] for _ in range(N)]

visited[0][0] = True
overlap[0][0][0][0] = True
q.append((0,0,0,0))

while q:
    time, x, y, prev = q.popleft()

    if time >= T:
        break

    cost = time + 1
    
    cases = directions[crosses[x][y][time % 4]]

    if prev != cases[0]:
        continue
    
    for case in cases:
        nx = x + dx[case]
        ny = y + dy[case]

        if nx < 0 or ny < 0 or nx >= N or ny >= N or overlap[nx][ny][cost % 4][case]:
            continue
        
        visited[nx][ny] = True
        overlap[nx][ny][cost % 4][case] = True
        q.append((cost, nx, ny, case))

answer = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            answer += 1

print(answer)