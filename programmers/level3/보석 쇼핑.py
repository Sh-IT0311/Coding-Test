def solution(gems):
    mydict = {}
    num_gems = len(gems)
    kinds = set(gems)
    num_kinds = len(kinds)
    
    
    small_interval = int(1e9)
    for i in range(num_gems):
        mydict[gems[i]] = i
        if len(mydict) == num_kinds:
            min_gem = min(mydict.items(), key = lambda x : x[1])[0]
            max_gem = max(mydict.items(), key = lambda x : x[1])[0]
            small_interval = mydict[max_gem] - mydict[min_gem] + 1
            answer = [mydict[min_gem] + 1, mydict[max_gem] + 1]
            break
    
    for i in range(mydict[max_gem],num_gems):
        mydict[gems[i]] = i
        if gems[i] == max_gem:
            pass
        
        elif gems[i] == min_gem:
            max_gem = min_gem
            min_gem = min(mydict.items(), key = lambda x : x[1])[0]
    
            temp = mydict[max_gem] - mydict[min_gem] + 1
            
            if temp < small_interval:
                small_interval = temp
                answer = [mydict[min_gem] + 1, mydict[max_gem] + 1]
                
        else:
            max_gem = gems[i]
            
            
    
    return answer