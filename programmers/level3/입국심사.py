def solution(n, times):
    answer = 0
    
    times.sort()
    start = times[0]
    end = start * n

    while start <= end:
        mid = (start + end) // 2
        result = 0
        for time in times:
            result += mid // time
            if result > n:
                break
        if result == n:
            answer = mid
            end = mid - 1
        elif result > n:
            answer = mid #result == n이 안나오는 경우도 있을듯.. 그럴땐 더 큰 상황을 취해야
            end = mid - 1
        else:
            start = mid + 1
        
    return answer