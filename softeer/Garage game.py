import sys
input = sys.stdin.readline
from collections import deque

ROUND = 3
N = int(input())
data = [[] for _ in range(N)]
for _ in range(ROUND * N):
    for i, color in enumerate(map(int, input().split())):
        data[i].append(color)

mat = list()
indices = [N] * N
for i in range(N):
    data[i].reverse()
    mat.append(data[i][:N])

answer = 6
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
def dfs(dup, rnd, value):
    global answer
    
    overlap = [[False] * N for _ in range(N)]
    neighbor = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i < N-1 and dup[i][j] == dup[i+1][j]:
                neighbor[i][j] = neighbor[i+1][j] = True
            if j < N-1 and dup[i][j] == dup[i][j+1]:
                neighbor[i][j] = neighbor[i][j+1] = True

            if not overlap[i][j]:
                overlap[i][j] = True
                
                if rnd == ROUND - 1 and not neighbor[i][j]:
                    answer = max(answer, value + 2)
                    continue

                color = dup[i][j]
                q = deque([(i, j)])
                visited = [set() for _ in range(N)]
                visited[i].add(j)

                cnt = 0
                top = bottom = i
                left = right = j

                while q:
                    x, y = q.popleft()
                    
                    overlap[x][y] = True
                    cnt += 1
                    top = min(top, x)
                    bottom = max(bottom, x)
                    left = min(left, y)
                    right = max(right, y)
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or ny < 0 or nx >= N or ny >= N or dup[nx][ny] != color:
                            continue

                        if ny not in visited[nx]:
                            visited[nx].add(ny)
                            q.append((nx, ny))
                if rnd < ROUND - 1:
                    mat = list()
                    for x in range(N):
                        temp = dup[x]
                        checked = visited[x]
    
                        for index in sorted(checked, reverse = True):
                            temp = temp[:index] + temp[index+1:]

                        temp += data[x][indices[x]:indices[x]+len(checked)]
                        indices[x] += len(checked)
                        mat.append(temp)

                    dfs(mat, rnd+1, value + cnt + (bottom - top + 1) * (right - left + 1))
    
                    for x in range(N):
                        indices[x] -= len(visited[x])
                        
                else:
                    answer = max(answer, value + cnt + (bottom - top + 1) * (right - left + 1))
    
    return None

dfs(mat, 0, 0)
print(answer)