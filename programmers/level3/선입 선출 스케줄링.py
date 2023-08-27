def solution(n, cores):
    #answer = 0
    c = len(cores)
    n -= c
    if n < 0:
        return n + c
    start,end = 0,min(cores) * n
    
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        memo = []
        for i,core in enumerate(cores):
            temp += (mid // core)
            if mid % core == 0:
                memo.append(i+1)
            
        if temp < n:
            start = mid + 1
        
        else:
            if temp - n < len(memo):
                answer = memo[-1 + n - temp]    
            end = mid - 1
        
    return answer