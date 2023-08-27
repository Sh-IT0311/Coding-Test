def solution(cookie):
    answer = 0
    n = len(cookie)
    
    for i in range(n-1):
        left = i
        right = i+1
        
        left_value = cookie[left]
        right_value = cookie[right]
        
        while True:
            if left_value == right_value:
                answer = max(answer, right_value)
                left -= 1
                if left < 0:
                    break
                left_value += cookie[left]
                right += 1
                if right >= n:
                    break
                right_value += cookie[right]
            elif left_value < right_value:
                left -= 1
                if left < 0:
                    break
                left_value += cookie[left]
            else:
                right += 1
                if right >= n:
                    break
                right_value += cookie[right]
    
    return answer