from itertools import product
from heapq import heappush, heappop

def solution(k, n, reqs):
    answer = 1e9

    for case in product(range(1, n - k + 2), repeat = k):
        if sum(case) == n:
            waiting = 0
            consults = [-1]
            
            for i in range(k):
                consults.append([0] * case[i])
                
            
            for a, b, c in reqs:
                now = heappop(consults[c])
            
                if now <= a:
                    heappush(consults[c], a + b)
                else:
                    waiting += now - a
                    heappush(consults[c], now + b)
                
            
            answer = min(answer, waiting)    
    
    return answer