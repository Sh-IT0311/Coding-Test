from collections import deque

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    n = len(food_times)
    index = set(range(n))
    data = deque(sorted([(food_times[i],i)for i in range(n)]))
    now = 0
    while True:
        num, idx = data.popleft()

        index.remove(idx)
        
        temp,now = num-now,num
        
        if k - temp * n >= 0:
            k -= temp * n
            if k == 0:
                break
        else:
            index.add(idx)
            break
        
        n -= 1
        while True:
            if data[0][0] == num:
                num,idx = data.popleft()
                index.remove(idx)
                n -= 1
            else:
                break

    index = list(index)
    index.sort()
    k %= n
    temp = 0
    for i in index:
        if temp == k:
            answer = i
            break
        temp += 1

    return answer + 1