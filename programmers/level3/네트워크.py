from collections import deque

def solution(n, computers):
    
    answer = 0
    
    while True:
        q = deque()
        flag = False
        for i in range(n):
            for j in range(n):
                if computers[i][j] == 1:
                    q.append((i,j))
                    computers[i][j] = 0
                    computers[j][i] = 0 
                    flag = True
            if flag:
                answer += 1
                break
        
        if len(q) == 0:
            break
        
        while q:
            x,y = q.popleft()
            for i in range(n):
                if computers[y][i] == 1:
                    computers[y][i] = 0
                    computers[i][y] = 0
                    q.append((y,i))

    return answer