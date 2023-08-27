def solution(board, skill):
    answer = 0
    
    rows = len(board)
    cols = len(board[0])
    
    save = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1: # down
            degree = -degree
        
        save[r1][c1] += degree
        save[r1][c2+1] += -degree
        save[r2+1][c1] += -degree
        save[r2+1][c2+1] += degree
    
    for row in range(rows):
        for col in range(1,cols):
            save[row][col] += save[row][col-1]
            
    for col in range(cols):
        for row in range(1,rows):
            save[row][col] += save[row-1][col]
    
    for row in range(rows):
        for col in range(cols):
            if board[row][col] + save[row][col] > 0:
                answer += 1
    
    return answer