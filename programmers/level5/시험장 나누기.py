def solution(k, num, links):
    n = len(num)
    
    temp = set(sum(links, []))
    root = sorted(set(range(n)) - temp).pop()    
    
    upper = [-1] * n
    q = [root]
    idx = 0
    while len(q) != idx:
        now = q[idx]
        a, b = links[now]
        if a != -1:
            q.append(a)
            upper[a] = now
            
        if b != -1:
            q.append(b)
            upper[b] = now
    
        idx += 1
    
    answer = sum(num)
    left, right = answer // k, answer
    while left <= right:
        mid = (left + right) // 2
        groups = dict(enumerate(num))
        idx = -1
    
        while len(q) != abs(idx):
            now = q[idx]
            idx -= 1
        
            parent = upper[now]
            
            if parent == upper[q[idx]]:
                other = q[idx]
                idx -= 1
                
                if groups[parent] + groups[other] + groups[now] <= mid:
                    groups[parent] += groups.pop(other) + groups.pop(now)
                    
                else:
                    now = min(now, other, key = lambda x : groups[x])
                
                    if groups[parent] + groups[now] <= mid:
                        groups[parent] += groups.pop(now)
                
            else:
                if groups[parent] + groups[now] <= mid:
                    groups[parent] += groups.pop(now)
        
        if len(groups) <= k:
            answer = max(groups.values())
            right = mid - 1
        
        else:
            left = mid + 1
        
    return answer