from heapq import heappop, heappush

def solution(alp, cop, problems):
    problems = [(0,0,1,0,1), (0,0,0,1,1)] + problems
    
    max_alp = max(problems, key = lambda x : x[0])[0]
    max_cop = max(problems, key = lambda x : x[1])[1]
    
    max_alp = max(max_alp, alp)
    max_cop = max(max_cop, cop)

    if alp == max_alp and cop == max_cop:
        return 0
    
    INF = int(1e9)
    costs = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    costs[alp][cop] = 0
    
    q = [(0, alp, cop)]

    while q:
        now, alp, cop = heappop(q)
        
        if costs[alp][cop] < now:
            continue
            
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp >= alp_req and cop >= cop_req:
                
                nalp = min(alp + alp_rwd, max_alp)
                ncop = min(cop + cop_rwd, max_cop)
                value = now + cost
                
                if value < costs[nalp][ncop]:
                    costs[nalp][ncop] = value
                    heappush(q, (value, nalp, ncop))
        
    return costs[max_alp][max_cop]