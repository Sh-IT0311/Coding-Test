def solution(n, m, x, y, r, c, k):
    answer = ''
    
    temp = k - abs(x-r) - abs(y-c)
    if temp < 0 or temp % 2 != 0:
        return 'impossible'
    
    flag = True
    temp = abs(y-c)
    while flag and x < n:
        if abs(x-r) + temp < k:
            x += 1
            k -= 1
            answer += 'd'
        else:
            flag = False
    
    temp = abs(x-r)
    while flag and y > 1:
        if temp + abs(y-c) < k:
            y -= 1
            k -= 1
            answer += 'l'
        else:
            flag = False
    
    if flag:
        k -= abs(x-r) + abs(y-c)
        answer += 'rl' * (k // 2) + 'r' * (c-y) + 'u' * (x-r)
        
    else:
        if x < r:
            answer += 'd' * (r-x)
        if y > c:
            answer += 'l' * (y-c)
        if y < c:
            answer += 'r' * (c-y)
        if x > r:
            answer += 'u' * (x-r)
    
    return answer