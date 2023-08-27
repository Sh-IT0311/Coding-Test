from collections import defaultdict
answer = set()

def dfs(banned_id, banned,i,num,data):
    global answer
    if len(data) == num:
        temp = list(data)
        temp.sort()
        answer.add(tuple(temp))
        return
    if i >= num:
        return
    
    temp = list(banned[banned_id[i]])
    
    for t in temp:
        n = len(data)
        data.add(t)
        if n != len(data):
            dfs(banned_id,banned,i+1,num,data)
            data.remove(t)
    

def solution(user_id, banned_id):
    global answer
    
    user = [[] for _ in range(9)]
    banned = defaultdict(set)
    
    for u in user_id:
        user[len(u)].append(u)
        
    
    for b in banned_id:
        for u in user[len(b)]:
            temp = 0
            for i in range(len(b)):
                if b[i] == '*':
                    temp += 1
                else:
                    if b[i] == u[i]:
                        temp += 1
            if temp == len(b):
                banned[b].add(u)
    
    num = len(banned_id)
    
    dfs(banned_id,banned,0,num,set())
    
    return len(answer)