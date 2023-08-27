from collections import deque

n , q = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())

    graph[a].append((b,c)) #destination, usado
    graph[b].append((a,c))

INF = int(1e9)

for _ in range(q):
    k , v = map(int,input().split())
    visited = [-1] * (n+1)
    q = deque()
    visited[v] = 1
    q.append((v,k,INF))
    count = 0
    while q:
        now, k,usado = q.popleft()
        for other in graph[now]:
            destination, other_usado = other
            if visited[destination] == -1:
                visited[destination] = 1
                real_usado = min(usado, other_usado)
                q.append((destination, k,real_usado))
                if real_usado >= k :
                    count += 1

    print(count)