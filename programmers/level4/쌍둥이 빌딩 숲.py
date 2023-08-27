def solution(n, count):
    mod = 1000000007
    dp = [0] * (count + 1)
    dp[1] = 1
    for i in range(2, n+1):
        cons = 2 * (i - 1)
        for j in range(count, 0, -1):
            dp[j] = (dp[j-1] + dp[j] * cons) % mod
    return dp[count]