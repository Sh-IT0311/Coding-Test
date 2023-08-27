def solution(n, s):
    if n > s:
        return [-1]
    
    t = s // n
    left = s % n
    
    temp = [t] * n
    for i in range(left):
        temp[i] += 1
    
    temp.reverse()
    
    return temp