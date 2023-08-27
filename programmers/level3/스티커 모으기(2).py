def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    case1 = sticker[:-1]
    case2 = sticker[1:]
    
    dp1 = [0] * (n-1)
    dp2 = [0] * (n-1)
    
    dp1[0] = case1[0]
    dp2[0] = case2[0]
    
    dp1[1] = max(case1[0], case1[1])
    dp2[1] = max(case2[0], case2[1])
    
    for i in range(2,n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + case1[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + case2[i])
    
    return max(dp1[-1], dp2[-1])