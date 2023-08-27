def solution(t):
    n = len(t)
    dp = [t[i].copy() for i in range(n)]
    
    for i in range(n-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + t[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + t[i+1][j+1])
    
    return max(dp[-1])