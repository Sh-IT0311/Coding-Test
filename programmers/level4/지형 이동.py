from collections import deque, defaultdict

def solution(land, height):
    answer = 0
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        
        if a < b:
            parent[b] = a
            
        else:
            parent[a] = b
    
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    n = len(land)
    visited = [[0] * n for _ in range(n)]
    now = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                now += 1
                visited[i][j] = now
                q = deque([(i,j)])
                
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                            
                        if visited[nx][ny] == 0 and abs(land[x][y] - land[nx][ny]) <= height:
                            visited[nx][ny] = now
                            q.append((nx,ny))
                            
    edges = defaultdict(lambda : 10001)
    for x in range(n):
        for y in range(n):
            for k in range(2):
                nx = x + dx[k]
                ny = y + dy[k]
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                    
                a,b = visited[nx][ny], visited[x][y]
                if a > b:
                    edges[(b,a)] = min(edges[b,a], abs(land[nx][ny] - land[x][y]))
                
                elif a < b:
                    edges[(a,b)] = min(edges[a,b], abs(land[nx][ny] - land[x][y]))
                    
    edges = [(edges[key], *key) for key in edges.keys()]
    edges.sort()
    
    parent = [i for i in range(now+1)]
    for c,a,b in edges:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += c
    
    return answer