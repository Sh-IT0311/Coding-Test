import sys
sys.setrecursionlimit(300000)
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())
current_edges = [[] for _ in range(N+1)]
reversed_edges = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    current_edges[x].append(y)
    reversed_edges[y].append(x)
S, T = map(int, sys.stdin.readline().split())

def dfs(now, edges, visited):
    for node in edges[now]:
        if node not in visited:
            visited.add(node)
            dfs(node, edges, visited)
    
start_current_visited = {S, T}
dfs(S, current_edges, start_current_visited)
start_reversed_visited = {T}
dfs(T, reversed_edges, start_reversed_visited)
start_current_visited = start_current_visited & start_reversed_visited

target_current_visited = {S, T}
dfs(T, current_edges, target_current_visited)
target_reversed_visited = {S}
dfs(S, reversed_edges, target_reversed_visited)
target_current_visited = target_current_visited & target_reversed_visited

print(len(start_current_visited & target_current_visited) - 2)