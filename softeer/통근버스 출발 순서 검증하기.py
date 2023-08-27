import sys

input = sys.stdin.readline
N = int(input())
buses = list(map(int,input().split()))

def solution(N, buses):
    answer = 0

    cnt = [[0] * N for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        value = buses[i]
        for j in range(i+1):
            cnt[value][j] = 1
    
    for i in range(N):
        for j in range(2, N+1):
            cnt[j][i] += cnt[j-1][i]
            
    for i in range(N-1):
        for j in range(i+1, N):
            if buses[i] < buses[j]:
                answer += cnt[buses[i]][j]
    
    return answer

print(solution(N, buses))