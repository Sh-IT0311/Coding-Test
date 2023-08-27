from heapq import heappush, heappop, heapify

def solution(n, works):
    if sum(works) <= n:
        return 0
    
    w = len(works)
    works = list(map(lambda x : -x, works))
    heapify(works)
    
    for _ in range(n):
        if works[0] != 0:
            heappush(works, heappop(works) + 1)
        # else:
            # break
    return sum([works[i] ** 2 for i in range(w)])