def solution(routes):
    answer = 0
    
    routes.sort()
    
    start , end = routes[0]
    flag = False
    
    for a, b in routes[1:]:
        if start <= a <= end:
            start = max(start,a)
            end = min(end, b)
        else:
            start ,end = a,b
            answer += 1
    
    answer += 1
    return answer