def solution(money):
    n = len(money)
    if n <= 3:
        return max(money[0] ,money[1], money[2])
    dp1 = [0] * (n-1)
    dp1[0],dp1[1] = money[0], max(money[0],money[1])
    dp2 = [0] * (n-1)
    dp2[0],dp2[1] = money[1], max(money[1],money[2])
    
    for i in range(2,n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i+1])
    
    return max(dp1[-1],dp2[-1])