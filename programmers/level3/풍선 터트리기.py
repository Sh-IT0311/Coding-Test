def solution(a):
    answer = 1
    index = min(range(len(a)), key = lambda x : a[x])
    
    left = a[:index]
    right = a[index+1:]

    if left:
        temp = left[0]
        answer += 1
        
        for i in left[1:]:
            if i < temp:
                temp = i
                answer += 1
 
    if right:
        temp = right[-1]
        answer += 1
        for i in right[-2::-1]:
            if i < temp:
                temp = i
                answer += 1
    
    return answer