def solution(target):
    INF = 100001
    dp = [[INF,0] for _ in range(max(target+1, 61))]
    
    conditions = set(range(1,21)) | {50}
    nothing = set(range(2,41,2)) | set(range(3,61,3))
    
    for value in conditions:
        temp = dp[value]
        temp[0] = 1
        temp[1] = 1
        
    for value in nothing:
        temp = dp[value]
        temp[0] = 1
        
    visited = conditions | nothing
    cases = list(visited)
    cases.sort()
    
    for i in range(1, target+1):
        if i in visited:
            continue
        
        now = dp[i]
        
        for case in cases:
            diff = i - case
            
            if diff < 1:
                break
                
            other = dp[diff]
            
            if other[0] + 1 < now[0]:
                now[0] = other[0] + 1
                if case in conditions:
                    now[1] = other[1] + 1
                else:
                    now[1] = other[1]
            
            elif other[0] + 1 == now[0]:
                if case in conditions:
                    now[1] = max(now[1], other[1] + 1)
                else:
                    now[1] = max(now[1], other[1])
    
    return dp[target]