from collections import deque

def solution(info, edges):
    answer = 1
    
    n = len(info)
    tree = [[] for _ in range(n)]
    for a,b in edges:
        tree[a].append(b)
    
    q = deque([(0,1,-1, [])])
    while q:
        now, s, w, wolves = q.popleft()
        
        w += 1
        if s <= w:
            continue
        
        queue = deque([now])
        while queue:
            status = queue.popleft()
            
            for _next in tree[status]:
                if info[_next]:
                    wolves.append(_next)
                else:
                    s += 1
                    queue.append(_next)
        
        answer = max(answer, s)   
        
        for i in range(len(wolves)):
            q.append((wolves[i], s, w, wolves[:i] + wolves[i+1:]))
        
    return answer