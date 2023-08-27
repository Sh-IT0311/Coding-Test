from itertools import product

def solution(clockHands):
    answer = float('inf')
    n = len(clockHands)

    data = [[0] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            data[i+1][j+1] = clockHands[i][j]
    
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    def dfs(x, cnt):
        nonlocal answer
        if x >= n+1:
            for y in range(1,n+1):
                if data[x-1][y] != 0:
                    break
            else:
                answer = min(answer, cnt)
            return

        temp = list()
        if x == n:
            end = x+1
        else:
            end = x+2
        for i in range(x-1, end):
            temp.append(data[i].copy())

        for y in range(1,n+1):
            value = (4 - data[x-1][y]) % 4

            if value != 0:
                cnt += value
                data[x][y] = (data[x][y] + value) % 4
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    data[nx][ny] = (data[nx][ny] + value) % 4

        dfs(x+1, cnt)

        for i in range(x-1, end):
            data[i] = temp[i-x+1]

    x = 1
    for case in product(range(4), repeat = n):
        cnt = 0
        temp = list()
        for i in range(x,x+2):
            temp.append(data[i].copy())
        
        for y, value in enumerate(case):
            y+=1
            if value != 0:
                cnt += value
                data[x][y] = (data[x][y] + value) % 4
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    data[nx][ny] = (data[nx][ny] + value) % 4

        dfs(x+1, cnt)

        for i in range(x,x+2):
            data[i] = temp[i-x]

    return answer