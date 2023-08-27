def solution(operations):
    q = [False] * 1000001
    max_value = -1
    min_value = int(1e9)
    num = 0
    for oper in operations:
        op = oper[0]
        value = int(oper[2:])
        
        if op == 'I':
            q[value] = True
            max_value = max(value, max_value)
            min_value = min(value, min_value)
            num += 1
        elif op == 'D':
            if num <= 0:
                continue
            num -= 1
            if num == 0:
                if value == 1:
                    q[max_value] = False
                else:
                    q[min_value] = False
                max_value = -1
                min_value = int(1e9)
                continue
            if value == 1:
                q[max_value] = False
                for i in range(max_value, min_value-1,-1):
                    if q[i]:
                        max_value = i
                        break
            else:
                q[min_value] = False
                for i in range(min_value, max_value+1,1):
                    if q[i]:
                        min_value = i
                        break
                
    if num > 0:
        return [max_value, min_value]
    
    return [0,0]