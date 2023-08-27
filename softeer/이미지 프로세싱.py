import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
data = []
for _ in range(H):
    data.append(list(map(int, input().split())))
Q = int(input())
queries = []
for _ in range(Q):
    queries.append(list(map(int, input().split())))

def solution(H, W, data, Q, queries):
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    
    for i,j,c in queries:
        i, j = i-1, j-1
        value = data[i][j]
        
        if value == c:
            continue
        
        data[i][j] = c
        q = deque([(i,j)])
        
        while q:
            x,y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx < 0 or ny < 0 or nx >= H or ny >= W:
                    continue
                    
                if data[nx][ny] == value:
                    data[nx][ny] = c
                    q.append((nx,ny))
    
    return data

result = solution(H,W, data, Q, queries)
for i in range(H):
    print(' '.join(map(str, result[i])))