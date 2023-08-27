from collections import deque

def rotate(n,temp):
    return sorted([(b,n-1-a) for a,b in temp])

def check(a,b):
    n = len(a)
    r,c = a[0][0] - b[0][0], a[0][1] - b[0][1]
    
    for i in range(1,n):
        if a[i][0] - b[i][0] != r or a[i][1] - b[i][1] != c:
            return False  
    return True       

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    
    g = [[] for _ in range(7)]
    t = [[] for _ in range(7)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                temp = [(i,j)]
                game_board[i][j] = 1
                q = deque([(i,j)])
                
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                            
                        if game_board[nx][ny] == 0:
                            temp.append((nx,ny))
                            game_board[nx][ny] = 1
                            q.append((nx,ny))
                            
                g[len(temp)].append(sorted(temp))
            
            if table[i][j] == 1:
                temp = [(i,j)]
                table[i][j] = 0
                q = deque([(i,j)])
                
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx < 0 or ny < 0 or nx >= n or ny >= n:
                            continue
                            
                        if table[nx][ny] == 1:
                            temp.append((nx,ny))
                            table[nx][ny] = 0
                            q.append((nx,ny))
                            
                t[len(temp)].append(tuple(sorted(temp)))
        
    overlap = set()    
    for i in range(1,7):
        for j in g[i]:
            flag = False
            for k in t[i]:
                if k not in overlap:
                    temp = k
                    for _ in range(4):
                        temp = rotate(n,temp)
                        if check(j,temp):
                            answer += i
                            overlap.add(k)
                            flag = True
                            break
                if flag:
                    break
                    
    return answer