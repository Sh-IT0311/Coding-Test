def solution(matrix_sizes):
    m = len(matrix_sizes)
    
    dp = [[float('inf')] * m for _ in range(m)]
    
    for i in range(m):
        dp[i][i] = 0
        
    for length in range(1, m):
        for index in range(m - length):
            for k in range(index, index + length):
                dp[index][index+length] = min(dp[index][index+length], dp[index][k] + dp[k+1][index+length] + matrix_sizes[index][0] * matrix_sizes[k][1] * matrix_sizes[index+length][1])
    
    return dp[0][-1]