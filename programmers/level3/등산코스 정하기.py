from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    INF = float('inf')
    intensities = [INF] * (n+1)
    
    graph = [[] for _ in range(n+1)]
    for a,b,c in paths:
        graph[a].append((c, b))
        graph[b].append((c, a))
        
    q = list()
    for gate in gates:
        intensities[gate] = 0
        q.append((0, gate))
        
    summits = set(summits)
    
    while q:
        intensity, now = heappop(q)
        
        if now in summits:
            continue
            
        if intensities[now] < intensity:
            continue
            
        for cost, _next in graph[now]:
            value = max(cost, intensity)
            
            if value < intensities[_next]:
                intensities[_next] = value
                heappush(q, (value, _next))
    
    answer = INF
    index = 0
    for summit in summits:
        if intensities[summit] < answer:
            index = summit
            answer = intensities[summit]
        elif intensities[summit] == answer:
            index = min(index, summit)
    
    return [index, answer]