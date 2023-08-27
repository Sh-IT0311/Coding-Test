def solution(n, s, a, b, fares):
    INF = int(1e9)
    dp = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        dp[i][i] = 0
    for q,w,e in fares:
        dp[q][w] = e
        dp[w][q] = e
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                temp = dp[i][k] + dp[k][j]
                if temp < dp[i][j]:
                    dp[i][j] = temp
    
    return min([dp[s][i] + dp[i][a] + dp[i][b] for i in range(1,n+1)])