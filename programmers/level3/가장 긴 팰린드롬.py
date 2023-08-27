def solution(s):
    answer = 1
    flag = False
    for i in range(len(s),1,-1):
        for j in range(len(s) - i + 1):
            t1 = s[j:j+i]
            t2 = t1[::-1]
            
            if t1 == t2 :
                answer = max(answer, i)
                flag = True
                break
        if flag:
            break
    
    return answer

def solution1(s):
    return len(s) if s[::-1] == s else max(solution(s[:-1]), solution(s[1:]))