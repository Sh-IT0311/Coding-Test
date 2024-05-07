import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N, M, K = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t, g = map(int, input().split())
    edges[s].append((e, t, g))

INF = float('inf')
distance = [[INF] * (N+1) for _ in range(K+1)]
distance[0][1] = 0
q = [(0, 0, 1)]

while q:
    cost, cnt, now = heappop(q)
    
    if distance[cnt][now] < cost:
        continue

    for e, t, g in edges[now]:
        r = cost % g
        if r == 0:
            value = cost + t
            if value < distance[cnt][e]:
                distance[cnt][e] = value
                heappush(q, (value, cnt, e))
        else:
            value = cost + t + g - r
            if value < distance[cnt][e]:
                distance[cnt][e] = value
                heappush(q, (value, cnt, e))
            
            if cnt < K:
                value = cost + t
                if value < distance[cnt+1][e]:
                    distance[cnt+1][e] = value
                    heappush(q, (value, cnt+1, e))
                    
result = min([distance[i][-1] for i in range(K+1)])
print(-1 if result == INF else result)
