from collections import deque

def solution(board):
    n = len(board)
    
    x1,y1 = 0,0
    x2,y2 = 0,1
    
    overlap = {((x1,y1), (x2,y2))} # sorted
    q = deque([((x1,y1),(x2,y2), 0)])
    
    while q:
        (x1, y1), (x2, y2), cnt = q.popleft()
        if x2 == n-1 and y2 == n-1:
            return cnt
        
        for direction in ((0,1),(0,-1), (1,0), (-1, 0)):
            nx1 = x1 + direction[0]
            ny1 = y1 + direction[1]
            
            if nx1 < 0 or ny1 < 0 or nx1 >= n or ny1 >= n:
                continue
            
            if board[nx1][ny1] != 0:
                continue
            
            nx2 = x2 + direction[0]
            ny2 = y2 + direction[1]
            
            if nx2 < 0 or ny2 < 0 or nx2 >= n or ny2 >= n:
                continue
                
            if board[nx2][ny2] != 0:
                continue
                
            temp = [(nx1,ny1),(nx2,ny2)]
            temp.sort()
            temp = tuple(temp)
            
            
            if temp not in overlap:
                overlap.add(temp)
                q.append(temp + (cnt+1,))       
        
        if x1 == x2:
            for d in (-1, 1):
                nx1 = x1 + d
                
                if nx1 < 0 or nx1 >= n:
                    continue
                    
                if board[nx1][y1] != 0:
                    continue
                    
                if board[nx1][y2] != 0:
                    continue
                    
                temp1 = [(x1,y1),(nx1,y1)]
                temp1.sort()
                temp1 = tuple(temp1)
                
                if temp1 not in overlap:
                    overlap.add(temp1)
                    q.append(temp1 + (cnt+1,))
                    
                temp2 = [(x2,y2),(nx1,y2)]
                temp2.sort()
                temp2 = tuple(temp2)
                
                if temp2 not in overlap:
                    overlap.add(temp2)
                    q.append(temp2 + (cnt+1,))
                
        elif y1 == y2:
            for d in (-1, 1):
                ny1 = y1 + d
                
                if ny1 < 0 or ny1 >= n:
                    continue
                    
                if board[x1][ny1] != 0:
                    continue
                    
                if board[x2][ny1] != 0:
                    continue
                    
                temp1 = [(x1,ny1),(x1,y1)]
                temp1.sort()
                temp1 = tuple(temp1)
                
                if temp1 not in overlap:
                    overlap.add(temp1)
                    q.append(temp1 + (cnt+1,))
                    
                temp2 = [(x2,y2),(x2,ny1)]
                temp2.sort()
                temp2 = tuple(temp2)
                
                if temp2 not in overlap:
                    overlap.add(temp2)
                    q.append(temp2 + (cnt+1,))
    return -1