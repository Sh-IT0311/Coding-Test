from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    blocks = ((2,((1,1),(1,2),(0,0),(1,0))), #3
             (1,((2,0),(1,1),(2,1),(0,1))), #2
             (1,((2,1),(1,0),(2,0),(0,0))), #2
             (2,((1,0),(1,1,),(1,2),(0,2))), #3
             (2,((1,0),(1,2),(1,1),(0,1)))) #3
    
    def check():
        
        for k,block in blocks:
            temp = set()
            for dx,dy in block:
                nx = x + dx
                ny = y + dy
                
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    break
                
                if board[nx][ny] == 0:
                    break
                    
                temp.add(board[nx][ny])
                if len(temp) > 1:
                    break
            else:
                return (k,block)
        
        return (False,False)
    
    def possible(x,y,temp):
        for dx,dy in temp:
            nx = x + dx
            ny = y + dy
            
            for k in range(nx-1,-1,-1):
                if board[k][ny] != 0:
                    return False
                
        return True
            
    after = deque()
    for x in range(n-1):
        for y in range(n-1):
            idx, check_list = check()
            if check_list:
                if possible(x,y,check_list[:idx]): 
                    answer += 1

                    for dx,dy in check_list:
                        board[x+dx][y+dy] = 0
                    
                    memo = len(after)
                    e = 0
                    while e != memo:
                        i, j , index, temp =  after.popleft()
                        if possible(i,j,temp[:index]):
                            answer += 1

                            for dx,dy in temp:
                                board[i+dx][j+dy] = 0
                        else:
                            after.append((i,j,index,temp))
                        e += 1
                else:  
                    after.append((x,y,idx,check_list))
    
    return answer