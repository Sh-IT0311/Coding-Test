import sys
from collections import defaultdict
sys.setrecursionlimit(300000)

def solution(n, lighthouse):
    graph = [[] for _ in range(n+1)]
    for a,b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    
    dp = defaultdict(lambda : [0,0])
    def init(prev, now):
        flag = False
        _sum = 0
        temp = 0
        for _next in graph[now]:
            if _next != prev:
                flag = True
                init(now, _next)
                _sum += dp[_next][1]
                temp += min(dp[_next])
        if flag:
            dp[now][1] = 1 + temp
            dp[now][0] = _sum
        else:
            dp[now][1] += 1
    init(0,1)
    return min(dp[1])