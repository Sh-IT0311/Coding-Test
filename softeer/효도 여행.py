import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000)

N, M = map(int, input().split())
S = input().strip()
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v, c = map(lambda x : int(x) if x.isdigit() else x, input().split())
    edges[u].append((v,c))
    edges[v].append((u,c))

dp = [[0] * (M+1) for _ in range(5001)]
result = 0
def dfs(prev, now, word):
    global result
    if len(word) > 0:
        i = len(word)
        for j in range(1, M+1):
            if word[i-1] == S[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
    for nxt, char in edges[now]:
        if prev != nxt:
            dfs(now, nxt, word + char)
            
dfs(0, 1, '')
print(result)
