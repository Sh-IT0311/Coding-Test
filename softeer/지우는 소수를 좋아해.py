import sys
from collections import defaultdict
from heapq import heappush, heappop
from math import sqrt

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
edges = defaultdict(lambda : defaultdict(lambda : INF))
for _ in range(M):
    a,b,c = map(int, input().split())
    edges[a][b] = min(edges[a][b], c)
    edges[b][a] = min(edges[b][a], c)
    
def solution(N, edges):
    distance = [INF] * (N+1)
    distance[1] = 0
    
    q = [(0, 1)]
    while q:
        dist, now = heappop(q)
        
        if distance[now] < dist:
            continue
        
        for _next in edges[now].keys():
            cost = max(dist, edges[now][_next])
            if cost < distance[_next]:
                distance[_next] = cost
                heappush(q, (cost, _next))
    
    answer = distance[-1] + 1
    while True:
        for i in range(2, int(sqrt(answer))+1):
            if answer % i == 0:
                break
        else:
            break
        
        answer += 1
    
    return answer

print(solution(N, edges))