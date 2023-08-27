import sys
sys.setrecursionlimit(300000)

def solution(nodeinfo):
    answer = [[],[]]
    n = len(nodeinfo)
    for i in range(n):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x : -x[1])
    def dfs(data):
        if data:
            answer[0].append(data[0][2])
            dfs([d for d in data[1:] if d[0] < data[0][0]])
            dfs([d for d in data[1:] if d[0] > data[0][0]])
            answer[1].append(data[0][2])
    dfs(nodeinfo)
    return answer