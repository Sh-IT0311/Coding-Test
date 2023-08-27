import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())

a = [-1] + list(map(int,input().split()))
b = [-1] + list(map(int,input().split()))

def solution(a,b):
    answer = 0
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(1,N+1):
        for j in range(1,M+1):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                answer = max(answer, dp[i][j])
                
    return answer

print(solution(a,b))