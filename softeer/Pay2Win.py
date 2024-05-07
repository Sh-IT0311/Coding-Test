import sys
input = sys.stdin.readline
from collections import defaultdict

N, K, H = map(int, input().split())
patterns = [list(map(int, input().split())) for _ in range(K)]
patterns.reverse()

INF = float('inf')
q = defaultdict(lambda : INF)
q[N] = 0
for i, j, x in patterns:
    cost1 = q.pop(i, INF)
    cost2 = q.pop(j, INF)
    
    if cost1 != INF:
        q[i] = min(q[i], cost1 + x)
        q[j] = min(q[j], cost1)

    if cost2 != INF:
        q[i] = min(q[i], cost2)
        q[j] = min(q[j], cost2 + x)

result = max(q.values()) + (H-1) *  q[N]
print(result)