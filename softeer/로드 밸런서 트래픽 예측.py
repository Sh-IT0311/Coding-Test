import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
edges = [tuple()]
for _ in range(N):
    edges.append(tuple(map(int, input().split())))

def solution(N, K, edges):
    answer = [0] * (N+1)
    indegree = [0] * (N+1)
    
    for num, *nexts in edges[1:]:
        for _next in nexts:
            indegree[_next] += 1
    
    answer[1] = K
    q = deque([1])
    while q:
        now = q.popleft()
        value = answer[now]
        
        num = edges[now][0]
        if num == 0:
            continue
        
        temp = [value // num] * num
        for i in range(value % num):
            temp[i] += 1
        
        for i in range(num):
            _next = edges[now][i+1]
            answer[_next] += temp[i]
            indegree[_next] -= 1
            if indegree[_next] == 0:
                q.append(_next)
    
    return answer[1:]

print(*solution(N,K,edges), end = ' ')