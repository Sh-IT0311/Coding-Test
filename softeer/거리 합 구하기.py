import sys
from collections import defaultdict

sys.setrecursionlimit(300000)

n = int(sys.stdin.readline().rstrip())
edges = list()
for _ in range(n-1):
    edges.append(tuple(map(int, sys.stdin.readline().rstrip().split())))


def solution(n, edges):
    answer = dict()


    graph = [dict() for _ in range(n+1)]
    for a,b,c in edges:
        graph[a][b] = c
        graph[b][a] = c


    start = 1
    result = 0
    cnt = defaultdict(lambda : 1)
    def init(prev, now):
        nonlocal result
        for next_ in graph[now].keys():
            if next_ != prev:
                init(now, next_)
                cnt[now] += cnt[next_]
        if prev != -1:
            result += cnt[now] * graph[prev][now]

    init(-1, start)
    answer[start] = result

    def dfs(prev, now):
        nonlocal result
        result -= cnt[now] * graph[prev][now]
        cnt[prev] = n - cnt[now]
        cnt[now] = n
        result += cnt[prev] * graph[now][prev]
        answer[now] = result
        for next_ in graph[now].keys():
            if prev != next_:
                dfs(now, next_)
        result -= cnt[prev] * graph[now][prev]
        cnt[now] = n - cnt[prev]
        cnt[prev] = n
        result += cnt[now] * graph[prev][now]


    for next_ in graph[start].keys():
        dfs(start, next_)

    return [answer[key] for key in range(1,n+1)]

result = solution(n, edges)
for r in result:
    print(r)