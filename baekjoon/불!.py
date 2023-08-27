def solution(R, C, maps):
    answer = 'IMPOSSIBLE'
    
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)


    npcs = list()
    fires = list()

    for i in range(R):
        for j in range(C):
            if maps[i][j] == 'J':
                npcs.append((i,j))

            elif maps[i][j] == 'F':
                fires.append((i,j))
    
    t = 0

    while True:
        t += 1
        tnpcs = list()
        tfires = list()

        for x, y in npcs:
            if maps[x][y] == 'F':
                continue

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    return t

                if maps[nx][ny] == '.':
                    maps[nx][ny] = 'J'
                    tnpcs.append((nx,ny))


        for x, y in fires:
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue

                if maps[nx][ny] in {'.', 'J'}:
                    maps[nx][ny] = 'F'
                    tfires.append((nx,ny))

        npcs = tnpcs
        fires = tfires

        if not npcs:
            break

    return answer

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]

print(solution(R, C, maps))