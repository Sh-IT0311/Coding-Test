# 이길 수 있으면 이겨야 되는 플레이를 진행함
    
def solution(board, aloc, bloc):
    
    rows = len(board)
    columns = len(board[0])
    
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)
    
    def dfs(x,y,ox,oy):
        if board[x][y] == 0:
            return 0
        
        status = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= rows or ny >= columns:
                continue
                
            if board[nx][ny] == 0:
                continue
                
            board[x][y] = 0
            now = dfs(ox, oy, nx, ny) + 1
            board[x][y] = 1
            
            if now % 2 == 1:
                if status % 2 == 1:
                    status = min(status, now)
                else:
                    status = now
                    
            else:
                if status % 2 == 0:
                    status = max(status, now)
        
        return status
    
    return dfs(aloc[0], aloc[1], bloc[0], bloc[1])