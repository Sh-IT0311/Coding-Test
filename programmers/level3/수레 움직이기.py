from itertools import product

def solution(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    answer = rows * cols
    
    dx = (0, 1, 0 ,-1)
    dy = (1, 0, -1, 0)
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                rsx, rsy = i, j
                
            elif maze[i][j] == 2:
                bsx, bsy = i, j
    
    rvisited = [[False] * cols for _ in range(rows)]
    rvisited[rsx][rsy] = True
    bvisited = [[False] * cols for _ in range(rows)]
    bvisited[bsx][bsy] = True
    
    def dfs(rx, ry, bx, by, cnt):
        nonlocal answer
        if answer <= cnt:
            return None
        
        if maze[rx][ry] == 3 and maze[bx][by] == 4:
            answer = min(answer, cnt)
            return None
        
        for rk, bk in product(range(4), range(4)):
            if maze[rx][ry] == 3:
                rflag = False
                rnx = rx
                rny = ry
                
            else:
                rflag = True
                rnx = rx + dx[rk]
                rny = ry + dy[rk]

                if rnx < 0 or rny < 0 or rnx >= rows or rny >= cols or maze[rnx][rny] == 5 or rvisited[rnx][rny]:
                    continue
            
            if maze[bx][by] == 4:
                bflag = False
                bnx = bx
                bny = by
                
            else:
                bflag = True
                bnx = bx + dx[bk]
                bny = by + dy[bk]

                if bnx < 0 or bny < 0 or bnx >= rows or bny >= cols or maze[bnx][bny] == 5 or bvisited[bnx][bny]:
                    continue
            
            if rnx == bnx and rny == bny:
                continue
            
            if rnx == bx and rny == by and bnx == rx and bny == ry:
                continue
            
            if rflag:
                rvisited[rnx][rny] = True
            if bflag:
                bvisited[bnx][bny] = True
            
            dfs(rnx, rny, bnx, bny, cnt + 1)
            
            if rflag:
                rvisited[rnx][rny] = False
            if bflag:
                bvisited[bnx][bny] = False
    
    dfs(rsx, rsy, bsx, bsy, 0)
    return 0 if answer == rows * cols else answer