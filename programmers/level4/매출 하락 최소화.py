from collections import defaultdict

def solution(sales, links):
    sales.insert(0, -1)
    n = len(sales)
    
    teams = defaultdict(list)
    for a,b in links:
        teams[a].append(b)
        
    costs = [[0,0] for _ in range(n)]
    
    def dfs(now):
        if now in teams.keys():
            _sum = 0
            _diff = float('inf')
            _flag = False
            for child in teams[now]:
                dfs(child)
                temp = costs[child]
                
                if temp[0] < temp[1]:
                    _sum += temp[0]
                    if not _flag:
                        _diff = min(_diff, temp[1] - temp[0])
                else:
                    _flag = True
                    _sum += temp[1]
                    
            costs[now][1] = sales[now] + _sum
            
            if _flag:
                costs[now][0] = _sum
            else:
                costs[now][0] = _sum + _diff
                
        else:
            costs[now][1] = sales[now]
    dfs(1)
    return min(costs[1])