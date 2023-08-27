from collections import defaultdict

def solution(numbers):
    costs = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3], 
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6], 
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5], 
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4], 
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5], 
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3], 
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2], 
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4], 
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2], 
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]
    
    INF = 1000000
    dp = [[INF] * 10 for _ in range(10)]
    dp[4][6] = 0

    for number in numbers:
        number = int(number)
    
        temp = [[INF] * 10 for _ in range(10)]
        for i in range(10):
            for j in range(10):
                if dp[i][j] != INF:
                    if i == number or j == number:
                        if dp[i][j] + 1 < temp[i][j]:
                            temp[i][j] = dp[i][j] + 1
                        
                    else:
                        ll = costs[i][number]
                        rl = costs[j][number]
                        
                        if dp[i][j] + rl < temp[i][number]:
                            temp[i][number] = dp[i][j] + rl
                        
                        if dp[i][j] + ll < temp[number][j]:
                            temp[number][j] = dp[i][j] + ll
                        
        dp = temp
    
    answer = INF
    for i in range(10):
        for j in range(10):
            answer = min(answer, dp[i][j])
    return answer