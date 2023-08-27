from collections import defaultdict, deque
from itertools import permutations, product

def solution(board, r, c):
    answer = int(1e9)
    
    loc = defaultdict(list)
    n = 4
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                loc[board[i][j]].append((i,j))
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    def bfs(s1,s2,e1,e2):
        temp = [[0] * n for _ in range(n)]
        q = deque([(s1,s2)])

        while q:
            x, y = q.popleft()
            if board[x][y] != 0:
                if s1 != x:
                    r = 1 if s1 > x else -1
                    flag = True
                    for i in range(x+r,s1,r):
                        if board[i][y] !=0:
                            if temp[x][y] > temp[i][y] + 1:
                                temp[x][y] = temp[i][y] + 1
                            flag = False
                            break
                    if flag:
                        if temp[x][y] > temp[s1][y] + 1:
                            temp[x][y] = temp[s1][y] + 1

                if s2 != y:
                    c = 1 if s2 > y else -1
                    flag = True
                    for i in range(y+c,s2,c):
                        if board[x][i] != 0:
                            if temp[x][y] > temp[x][i] + 1:
                                temp[x][y] = temp[x][i] + 1
                            flag = False
                            break
                    if flag:
                        if temp[x][y] > temp[x][s2] + 1:
                            temp[x][y] = temp[x][s2] + 1
            if x == 0:
                for i in range(1, s1):
                    flag = True
                    if board[i][y] != 0:
                        if temp[x][y] > temp[i][y] + 1:
                            temp[x][y] = temp[i][y] + 1
                        flag = False
                        break
                    if flag:
                        if temp[x][y] > temp[s1][y] + 1:
                            temp[x][y] = temp[s1][y] + 1
            elif x == n-1:
                for i in range(n-2, s1, -1):
                    flag = True
                    if board[i][y] != 0:
                        if temp[x][y] > temp[i][y] + 1:
                            temp[x][y] = temp[i][y] + 1
                        flag = False
                        break
                    if flag:
                        if temp[x][y] > temp[s1][y] + 1:
                            temp[x][y] = temp[s1][y] + 1
            if y == 0:
                for i in range(1, s2):
                    flag = True
                    if board[x][i] != 0:
                        if temp[x][y] > temp[x][i] + 1:
                            temp[x][y] = temp[x][i] + 1
                        flag = False
                        break
                    if flag:
                        if temp[x][y] > temp[x][s2] + 1:
                            temp[x][y] = temp[x][s2] + 1
            elif y == n-1:
                for i in range(n-2, s2,-1):
                    flag = True
                    if board[x][i] != 0:
                        if temp[x][y] > temp[x][i] + 1:
                            temp[x][y] = temp[x][i] + 1
                        flag = False
                        break
                    if flag:
                        if temp[x][y] > temp[x][s2] + 1:
                            temp[x][y] = temp[x][s2] + 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx == s1 and ny == s2:
                    continue

                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue

                if temp[nx][ny] == 0:
                    q.append((nx,ny))
                    temp[nx][ny] = temp[x][y] + 1

        return temp[e1][e2]
    
    overlap = set()
    def dfs(row,column,cost):
        nonlocal answer
        
        if len(overlap) == len(loc):
            answer = min(answer, cost)
        
        for key,value in loc.items():
            if key not in overlap:
                overlap.add(key)
                r1,c1 = value[0]
                r2,c2 = value[1]
                
                temp1 = bfs(row,column, r1,c1) + bfs(r1,c1,r2,c2)
                temp2 = bfs(row,column, r2,c2) + bfs(r2,c2,r1,c1)
                
                board[r1][c1] = 0
                board[r2][c2] = 0
                
                dfs(r2,c2,cost + temp1)
                dfs(r1,c1,cost+temp2)
                
                board[r1][c1] = key
                board[r2][c2] = key
                            
                overlap.remove(key)
     
    dfs(r,c,0)
    
    return answer + len(loc) * 2