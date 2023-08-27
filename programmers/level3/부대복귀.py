from heapq import heappop, heappush

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n+1)]
    for a,b in roads:
        graph[a].append((b,1))
        graph[b].append((a,1))
    
    INF = 100001
    distance = [INF] * (n+1)
    distance[destination] = 0
    
    q = [(0, destination)]
    while q:
        dist, now = heappop(q)
        
        if distance[now] < dist:
            continue
            
        for _next, value in graph[now]:
            cost = dist + value
            if cost < distance[_next]:
                distance[_next] = cost
                heappush(q, (cost, _next))
    
    for source in sources:
        if distance[source] == INF:
            answer.append(-1)
        else:
            answer.append(distance[source])
    return answer