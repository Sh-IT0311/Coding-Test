def solution(stones, k):
    answer = 0
    left, right = 1, int(2e8)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt >= k:
                    break
            else:
                cnt = 0
        else:
            left = mid + 1
            answer = mid
            continue
        right = mid - 1
    return answer