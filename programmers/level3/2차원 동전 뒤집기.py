from collections import deque

def solution(beginning, target):
    rows = len(beginning)
    columns = len(beginning[0])
    
    bl = sum(beginning, [])
    tl = sum(target , [])
    
    n = len(bl)
    values = dict()
    for i in range(n+1):
        values[i] = pow(2,i)
    
    bv = 0
    tv = 0
    for i in range(n):
        bv += bl[i] * values[i]
        tv += tl[i] * values[i]
    
    rvalues = list()
    cvalues = list()
    
    temp = 0
    for i in range(columns, n+1, columns):
        rvalues.append(values[i] - 1 - temp)
        temp += rvalues[-1]
    
    for j in range(columns):
        temp = 0
        for i in range(j, n, columns):
            temp += values[i]
        cvalues.append(temp)
    
    overlap = {bv}
    q = deque([(0, bv)])
    
    while q:
        cnt, now = q.popleft()
        
        if now == tv:
            return cnt
        
        for rvalue in rvalues:
            temp = now ^ rvalue
            if temp not in overlap:
                overlap.add(temp)
                q.append((cnt+1, temp))
                
        for cvalue in cvalues:
            temp = now ^ cvalue
            if temp not in overlap:
                overlap.add(temp)
                q.append((cnt+1, temp))
    
    return -1