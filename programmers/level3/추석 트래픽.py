def solution(lines):
    starts = list()
    ends = list()
    n = len(lines)
    for line in lines:
        _, time, p = line.split()
        
        h, m, s = map(float, time.split(':'))
        p = float(p[:-1]) * 1000
        
        end = h * 3600000 + m * 60000 + s * 1000
        start = int(end - p + 1)
        if start < 0:
            start = 0
            
        end = int(end) + 1000
        
        starts.append(start)
        ends.append(end)
    
    starts.sort()
    #ends.sort()
    
    si = 1
    ei = 0
    num = 1
    answer = 1
    
    while si < n:
        if starts[si] < ends[ei]:
            si += 1
            num += 1
            answer = max(answer, num)
        elif starts[si] > ends[ei]:
            ei += 1
            num -= 1
        elif starts[si] == ends[ei]:
            si += 1
            ei += 1
    
    
    return answer