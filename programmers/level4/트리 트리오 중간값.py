import sys
sys.setrecursionlimit(300000)

def solution(n, edges):
    graph = [[] for _ in range(n+1)]
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(prev, now, cnt):
        nonlocal max_length, max_list
        flag = False
        for _next in graph[now]:
            if _next != prev:
                flag = True
                dfs(now, _next, cnt + 1)
                
        if not flag:
            if max_length < cnt:
                max_length = cnt
                max_list = [now]
                
            elif max_length == cnt:
                max_list.append(now)
    
    max_list = list()
    max_length = -1
    dfs(0,1,0)
    
    start = max_list[-1]
    max_list = list()
    max_length = -1
    dfs(0, start, 0)
    
    if len(max_list) > 1:
        return max_length
    
    start = max_list[-1]
    max_list = list()
    max_length = -1
    dfs(0, start, 0)
    
    if len(max_list) > 1:
        return max_length
    else:
        return max_length - 1
    