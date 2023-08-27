def solution(e, starts):
    dp = [1] * (e+1)
    for i in range(2, e+1):
        for j in range(i, e+1, i):
            dp[j] += 1
    
    _max = dp[-1]
    index = [e]
    for i in range(e-1, 0 , -1):
        if _max <= dp[i]:
            _max = dp[i]
            index.append(i) 
        
        else:
            index.append(index[-1])     
    
    index.append(0)
    index.reverse()

    return [index[start] for start in starts]