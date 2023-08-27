from collections import deque

def solution(n, path, order):
    tree = [[] for _ in range(n)]
    for a,b in path:
        tree[a].append(b)
        tree[b].append(a)
        
    before = dict()
    after = dict()
    for a,b in order:
        if a != 0 and b == 0:
            return False
        after[a] = b
        before[b] = a
    
    q = deque([0])
    visited = {0}
    save = set()
    while q:
        now = q.popleft()
        
        for child in tree[now]:
            if child not in visited:
                if child in before.keys() and before[child] not in visited:
                    save.add(before[child])
                else:
                    q.append(child)
                    visited.add(child)
                                            
        if now in save:
            save.remove(now)
            q.append(after[now])
            visited.add(after[now])
    
    return len(visited) == n