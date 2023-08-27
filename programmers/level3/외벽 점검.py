from collections import deque

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    visited = {tuple(weak)}
    for i in range(len(dist)):
        d = dist[i]
        for _ in range(len(q)):
            current = q.popleft()
            for p in current:
                l = p
                r = (p + d) % n
                
                if l < r:
                    temp = [x for x in current if x < l or x > r]
    
                else:
                    temp = [x for x in current if x < l and x > r]
             
                if len(temp) == 0:
                    return (i + 1)
                
                temp = tuple(temp)
                if temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))
                     
    return -1