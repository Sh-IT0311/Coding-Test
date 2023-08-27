def solution(arr):
    n = len(arr) // 2 + 1
    INF = 100001
    
    max_dp = [[-INF] * n for _ in range(n)]
    min_dp = [[INF] * n for _ in range(n)]
    for i in range(n):
        max_dp[i][i] = int(arr[i*2])
        min_dp[i][i] = int(arr[i*2])
        
    for length in range(1,n):
        for index in range(n-length):
            for k in range(index, index+length):
                if arr[k*2+1] == '+':
                    max_dp[index][index+length] = max(max_dp[index][index+length], max_dp[index][k] + max_dp[k+1][index+length])
                    min_dp[index][index+length] = min(min_dp[index][index+length], min_dp[index][k] + min_dp[k+1][index+length])
                else:
                    max_dp[index][index+length] = max(max_dp[index][index+length], max_dp[index][k] - min_dp[k+1][index+length])
                    min_dp[index][index+length] = min(min_dp[index][index+length], min_dp[index][k] - max_dp[k+1][index+length])         
    return max_dp[0][-1]