def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = int(1e9)
    overlap = set()    
    
    def dfs(now,count):
        nonlocal answer
        if now == target:
            answer = min(answer, count)
            return
        
        for word in words:
            if word not in overlap:
                temp = zip(word,now)
                cnt = 0

                for a,b in temp:
                    if a != b:
                        cnt += 1

                if cnt == 1:
                    overlap.add(word)
                    dfs(word,count + 1)
                    overlap.remove(word)
    
    dfs(begin, 0)
    return answer