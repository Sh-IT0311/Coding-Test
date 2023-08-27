import sys
from collections import defaultdict

input = sys.stdin.readline

N,B = map(int, input().split())
performances = list(map(int, input().split()))

def solution(N, B, performances):
    answer = 0
    
    performances.sort()
    left = 1
    right = int(2e9)
    
    caching = defaultdict(lambda : temp ** 2)
    
    while left <= right:
        mid = (left + right) // 2
        cost = 0
    
        for performance in performances:
            if mid <= performance:
                break
            else:
                temp = mid - performance
                cost += caching[temp]
                if cost > B:
                    break
    
        if cost > B:
            right = mid - 1
            
        else:
            left = mid + 1
            answer = max(answer, mid)
    
    return answer

print(solution(N,B,performances))