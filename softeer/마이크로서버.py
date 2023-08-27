import sys
from heapq import heappush, heappop
from math import ceil

input = sys.stdin.readline

def solution(N, services):
    answer = 0
    
    start = 0
    end = N-1
    
    services.sort()
    
    while end >= 0 and services[end] > 600:
        answer += 1
        end -= 1
    
    cnt_600 = 0
    while end >= 0 and services[end] == 600:
        cnt_600 += 1
        end -= 1
        
    cnt_300 = 0
    while start < N and services[start] == 300:
        cnt_300 += 1
        start += 1
        
    temp = min(cnt_300, cnt_600)
    answer += cnt_600
    cnt_300 -= temp
    
    while start < end:
        answer += 1
        if services[start] + services[end] <= 900:
            start += 1
            end -= 1
        else:
            end -= 1
            if cnt_300 > 0:
                cnt_300 -= 1
    
    if start == end:
        answer += 1
        if cnt_300 > 0:
            cnt_300 -= 1
        
    q, r = divmod(cnt_300, 3)
    answer += q
    answer += ceil(r / 2)
    
    return answer

T = int(input())
for _ in range(T):
    N = int(input())
    services = list(map(int, input().split()))
    print(solution(N, services))