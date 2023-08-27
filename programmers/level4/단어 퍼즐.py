def solution(strs, t):
    answer = 0
    n = len(t)
    sizes = set()
    alpha = set()
    for c in strs:
        sizes.add(len(c))
        alpha.add(c)

    INF = 20001
    dp = [INF] * (n+1)
    dp[0] = 0
    for i in range(n):
        for size in sizes:
            if i + size <= n and t[i:i+size] in alpha:
                dp[i+size] = min(dp[i+size], dp[i] +1)

                
    return -1 if dp[-1] ==  INF else dp[-1]