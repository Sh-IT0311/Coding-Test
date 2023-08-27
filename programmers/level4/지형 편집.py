def solution(land, P, Q):
    land = sum(land, [])
    land.sort()
    l = len(land)
    
    cost = (sum(land) - land[0] * l) * Q
    answer = cost
    
    for i in range(1, l):
        if land[i] != land[i-1]:
            temp = land[i] - land[i-1]
            cost += temp * i * P - temp * (l-i) * Q
            if cost < answer:
                answer = cost
            else:
                break
    return answer