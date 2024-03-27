import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = list()
ghosts = list()
for i in range(n):
    matrix.append(list(input().strip()))
    for j in range(m):
        if matrix[i][j] == 'D':
            ex, ey = i, j
        elif matrix[i][j] == 'N':
            sx, sy = i, j
        elif matrix[i][j] == 'G':
            ghosts.append((i, j))

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)
checked = {'G', '#', 'N'}
q = [(sx, sy)]
gq = ghosts
while q:
    if matrix[ex][ey] == 'N':
        print('Yes')
        exit()
        
    gtemp = list()
    for gx, gy in gq:
        for k in range(4):
            gnx = gx + dx[k]
            gny = gy + dy[k]

            if gnx < 0 or gny < 0 or gnx >= n or gny >= m:
                continue

            if matrix[gnx][gny] != 'G':
                matrix[gnx][gny] = 'G'
                gtemp.append((gnx, gny))
    gq = gtemp
    if matrix[ex][ey] == 'G':
        print('No')
        exit()

    temp = list()
    for x, y in q:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
    
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
    
            if matrix[nx][ny] in checked:
                continue
    
            matrix[nx][ny] = 'N'
            temp.append((nx, ny))
    q = temp
    
print('No')