from collections import deque

def solution(board):
    n = len(board)
    costs = [[int(1e9)] * n for _ in range(n)]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    costs[0][0] = 0
    q = deque()
    if board[1][0] != 1:
        q.append(((1,2,1,0)))
        costs[1][0] = 1
    
    if board[0][1] != 1:
        q.append((1,0,0,1))
        costs[0][1] = 1
        
    while q:
        cost, direction, x, y = q.popleft()
        
        if costs[x][y] + 4 < cost:
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue
                
            value = 1 if direction == i else 6
            
            if cost + value < costs[nx][ny] + 4:
                q.append((cost + value, i, nx, ny))
            
            if cost + value < costs[nx][ny]:
                costs[nx][ny] = cost + value
        
    return costs[n-1][n-1] * 100