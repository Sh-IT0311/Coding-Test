from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    graph = [[0] * 102 for _ in range(102)]
    
    max_c, min_c = -1, 1
    max_r, min_r = -1, 1
    
    for c1,r1,c2,r2 in rectangle:
        if c1 < min_c:
            min_c = c1
        if max_c < c2:
            max_c = c2
            
        if r1 < min_r:
            min_r = r1
        if max_r < r2:
            max_r = r2
        
        
        for i in range(r1*2,r2*2+1):
            for j in range(c1*2,c2*2+1):
                graph[i][j] = 1
            
            
    dx = [0,1,0,-1,1,1,-1,-1]
    dy = [1,0,-1,0,-1,1,-1,1]
    for i in range(min_r * 2, max_r * 2 +1):
        for j in range(min_c * 2, max_c * 2 + 1):
            for k in range(8):
                if graph[i][j] and graph[i+dx[k]][j+dy[k]] == 0:
                    graph[i][j] = 2
                    break
    
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque([(0,characterY, characterX)])
    graph[characterY][characterX] += 1
    while q:
        cnt, x,y = q.popleft()
        
        if x == itemY and y == itemX:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if graph[nx][ny] == 2:
                q.append((cnt+0.5,nx,ny))
                graph[nx][ny] += 1
    
            
    
    return -1