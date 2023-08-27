from collections import defaultdict

def solution(tickets):
    answer = ['ICN']
    target = len(tickets) + 1
    
    edges = defaultdict(list)
    for a,b in tickets:
        edges[a].append(b)
    
    overlap = dict()
    for key in edges.keys():
        edges[key].sort()
        overlap[key] = [False] * len(edges[key])
    
    flag = False
    def dfs(now):
        nonlocal flag
        if len(answer) == target:
            flag = True
            return

        for i in range(len(edges[now])):
            if not overlap[now][i]:
                overlap[now][i] = True
                answer.append(edges[now][i])
                dfs(edges[now][i])
                if flag:
                    return
                answer.pop()
                overlap[now][i] = False
    
    dfs('ICN')
    return answer