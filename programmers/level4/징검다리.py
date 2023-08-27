def solution(distance, rocks, n):
    answer = 0
    
    rocks.sort()
    rocks.append(distance)
    r = len(rocks)
    start,end = 1,distance
    
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        prev = 0
        flag = False
        for i in range(r):
            if rocks[i] - prev < mid:
                if rocks[i] != distance:
                    cnt += 1
                    if cnt > n:
                        break
                else:
                    flag = True
            else:
                prev = rocks[i]
        print(mid, cnt)
        if cnt > n:
            end = mid -1
            
        else:
            start = mid + 1
            if flag:
                answer = max(answer,distance - prev)
            else:
                answer = mid
    
    return answer