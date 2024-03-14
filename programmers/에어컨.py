def solution(temperature, t1, t2, a, b, onboard):
    if t1 <= temperature <= t2:
        return 0
    
    if temperature < t1:
        temperature = t2 + t1 - temperature
    t1, t2, temperature = t1 + 10, t2 + 10, temperature + 10
    n = len(onboard)
    INF = 1e5
    dp = [[INF] * (temperature + 1) for _ in range(n+1)]
    dp[0][temperature] = 0
    
    for time in range(n):
        for temp in range(t1, temperature+1):
            if dp[time][temp] != INF:
                if onboard[time] and (t2 < temp) or (temp < t1):
                    continue
                
                if temp > t1:
                    dp[time+1][temp-1] = min(dp[time+1][temp-1], dp[time][temp] + a)
                    
                if temp <= t2:
                    dp[time+1][temp] = min(dp[time+1][temp], dp[time][temp] + b)
                    
                if temp <= temperature:
                    _next = min(temp+1, temperature)
                    dp[time+1][_next] = min(dp[time+1][_next], dp[time][temp])

    return min(dp[-1])