import heapq

def solution(n, edge):
    answer = 0
    v = len(edge)
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    for a,b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
        
    h = []
    heapq.heappush(h,(0,1))
    distance[1] = 0
    
    while h:
        dist, now = heapq.heappop(h)
        
        if distance[now] < dist:
            continue
            
        for arr, cost in graph[now]:
            value = cost + dist
            if value < distance[arr]:
                distance[arr] = value
                heapq.heappush(h,(value,arr))
        
    max_value = max(distance[1:])
    for d in distance[1:]:
        if d == max_value:
            answer+=1
    return answer