n,s = map(int, input().split())
data = list(map(int, input().split()))

answer = int(1e9)
    
start, end = 0, 0
value = data[start]
n = len(data)
    
while end < n:
    if value >= s:
        answer = min(answer, end - start + 1)
        
    if value <= s:
        end += 1
        if end == n:
            break
        value += data[end]
            
    elif value > s:
        value -= data[start]
        start += 1
            
    if start > end:
        end += 1
        if end == n:
            break
        value += data[end]
        
    
print(0 if answer == int(1e9) else answer)