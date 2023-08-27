import sys
sys.setrecursionlimit(300000)

def solution(a, edges):
    if sum(a) != 0:
        return -1
    
    answer = 0
    n = len(a)
    graph = [[] for _ in range(n)]
    
    for q,w in edges:
        graph[q].append(w)
        graph[w].append(q)
        
    start = 0  
    def dfs(now, prev):
        nonlocal answer
        for next_ in graph[now]:
            if next_ != prev:
                dfs(next_, now)
        
        if prev != -1:
            a[prev] += a[now]
            answer += a[now]if a[now] >= 0 else -a[now]
            #a[now] = 0
        return
    
    dfs(start, -1)
    
    return answer