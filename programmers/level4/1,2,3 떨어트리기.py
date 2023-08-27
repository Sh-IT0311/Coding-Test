def solution(edges, target):
    n = len(target)
    target.insert(0, 0)
    
    graph = [[] for _ in range(n+1)]
    for a,b in edges:
        graph[a].append(b)
        
    cnt = [0] * (n+1)
    leaves = 0
    for i in range(1,n+1):
        graph[i].sort()
        cnt[i] = len(graph[i])
        
        if cnt[i] == 0 and target[i] != 0:
            leaves +=1
        
    direction = [0] * (n+1)
    values = [0] * (n+1)
    orders = list()
    overlap = set()
    while True:
        now = 1
        while True:
            if cnt[now] == 0:
                break
                
            temp = graph[now][direction[now]]
            direction[now] = (direction[now] + 1) % cnt[now]
            now = temp
            
        if target[now] == 0:
            if len(overlap) == leaves:
                break
        
        orders.append(now)
        values[now] += 1
        if values[now] <= target[now] <= values[now] * 3:
            overlap.add(now)
        elif target[now] < values[now]:
            return [-1]
        
        if len(overlap) == leaves:
            break
    
    answer = []
    nums = dict()
    for now in orders:
        if now not in nums.keys():
            q, r = divmod(target[now] - values[now], 2)
            nums[now] = [3] * q + [2] * r + [1] * (values[now] - q - r)
        answer.append(nums[now].pop())
        
    return answer