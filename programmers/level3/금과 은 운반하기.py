def solution(a, b, g, s, w, t):
    n = len(g)
    _sum = a+b
    answer = int(4e14)
    
    left = 0
    right = answer
    while left <= right:
        mid = (left + right) // 2
        cases = list()
        
        for i in range(n):
            if t[i] <= mid:
                temp = mid - t[i]
                cases.append((int(temp // (2 * t[i])) + 1) * w[i])
            else:
                cases.append(0)

        
        possible = 0
        golds = 0
        silvers = 0
        for i in range(n):
            gtemp = min(g[i], cases[i])
            stemp = min(s[i], cases[i])
            golds += gtemp
            silvers += stemp
            possible += min(gtemp + stemp, cases[i]) 
            
        if possible >= _sum and golds >= a and silvers >= b:
            answer = min(answer, mid)
            right = mid - 1
            
        else:
            left = mid + 1
        
    return answer