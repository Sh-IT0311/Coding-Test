import sys
input = sys.stdin.readline

R, C = map(int, input().split())
matrix = list()
rains = list()
for i in range(R):
    matrix.append(list(input().strip()))
    for j in range(C):
        if matrix[i][j] == 'H':
            ex, ey = i, j
    
        elif matrix[i][j] == 'W':
            sx, sy = i, j

        elif matrix[i][j] == '*':
            rains.append((i, j))

if matrix[sx][sy] == 'H':
    print(0)
    exit()

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

q = [(sx, sy)]
rq = rains
time = 0
checked_rain = {'H', 'X', '*'}
checked_car = {'W', '*', 'X'}
while True:
    time += 1
    rtemp = list()
    for rx, ry in rq:
        for k in range(4):
            rnx = rx + dx[k]
            rny = ry + dy[k]
    
            if rnx < 0 or rny < 0 or rnx >= R or rny >= C:
                continue

            if matrix[rnx][rny] in checked_rain:
                continue

            matrix[rnx][rny] = '*'
            rtemp.append((rnx, rny))
    rq = rtemp
    
    temp = list()
    for x, y in q:

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue

            if matrix[nx][ny] in checked_car:
                continue

            if matrix[nx][ny] == 'H':
                print(time)
                exit()
                
            matrix[nx][ny] = 'W'
            temp.append((nx, ny))

    q = temp
    if len(q) == 0:
        print('FAIL')
        exit()