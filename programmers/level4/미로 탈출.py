# bitmasking -> 각 trap node의 on / off 상태 및 해당 경우(예) 2번,3번 노드만 켜진경우)를 나타냄
from collections import defaultdict
from heapq import heappush, heappop

def solution(n, start, end, roads, traps):
    t = len(traps)
    traps_dict = dict()
    for i in range(t):
        traps_dict[traps[i]] = 2 ** i
    
    original = defaultdict(lambda : defaultdict(lambda : 3001))
    reverse = defaultdict(lambda : defaultdict(lambda : 3001))
    for q,w,e in roads:
        original[q][w] = min(original[q][w], e)
        reverse[w][q] = min(reverse[w][q], e)
    
    INF = int(1e9)
    distance = [[INF] * pow(2, t) for _ in range(n+1)]
    
    q = [(0, start, 0, 0)]
    distance[start][0] = 0
    
    while q:
        dist, now, status, prev = heappop(q)
        
        if distance[now][status] < dist:
            continue
        
        flag = False
        if now in traps_dict.keys():
            if bool(traps_dict[now] & status):
                flag = True
        
        # 현재 노드가 (일반, off)? on? + 다음 노드가 일반? off? on? -> cur, rev 결정
        cur = reverse[now] if flag else original[now]
        for node in cur.keys():
            if node in traps_dict.keys():
                if not bool(traps_dict[node] & status):
                    temp = dist + cur[node]
                    next_stage = traps_dict[node] | status
                    if temp < distance[node][next_stage]:
                        distance[node][next_stage] = temp
                        heappush(q, (temp, node, next_stage, status))
            else:
                temp = dist + cur[node]
                if temp < distance[node][status]:
                    distance[node][status] = temp
                    heappush(q, (temp, node, status, status))
            
        rev = original[now] if flag else reverse[now]
        for node in rev.keys():
            if node in traps_dict.keys():
                if bool(traps_dict[node] & status):
                    temp = dist + rev[node]
                    next_stage = traps_dict[node] ^ status
                    if temp < distance[node][next_stage]:
                        distance[node][next_stage] = temp
                        heappush(q, (temp, node, next_stage, status))
        
    return min(distance[end])