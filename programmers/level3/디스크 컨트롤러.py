from heapq import heappush, heappop, heapify

def solution(jobs):
    n = len(jobs)
    heapify(jobs)
    
    now = 0
    answer = 0
    load = list()
    
    while jobs:
        while jobs and jobs[0][0] <= now:
            temp = heappop(jobs)
            heappush(load,(temp[1],temp[0]))    
          
        if load:
            temp = heappop(load)
            answer += temp[0] + now - temp[1]
            now += temp[0]
            
        elif jobs:
            temp = heappop(jobs)
            heappush(load, (temp[1],temp[0]))
            now = temp[0]
        
    while load:
        temp = heappop(load)
        answer += temp[0] + now - temp[1]
        now += temp[0]
        
    return answer // n