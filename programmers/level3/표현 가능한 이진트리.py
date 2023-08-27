from math import log2, ceil

def solution(numbers):
    answer = []
    
    def dfs(substr):
        nonlocal flag
        if not flag:
            return False
        
        if len(substr) == 1:
            return substr =='1'
            
        s = len(substr) // 2
        left = dfs(substr[:s])
        right = dfs(substr[s+1:])
        
        if left or right:
            if substr[s] == '1':
                return True
            else:
                flag = False
                return False
            
        else:
            return substr[s] == '1'
    
    for number in numbers:
        value = format(number, 'b')
        now = len(value)
        
        length = 2 ** ceil(log2(now + 1)) - 1
        data = '0' * (length - now) + value
        
        if length == 1:
            answer.append(1)
        
        else:
            flag = True
            dfs(data)
            answer.append(int(flag))
        
    return answer