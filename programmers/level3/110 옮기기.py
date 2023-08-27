def solution(s):
    answer = []
   
    for string in s:
        temp = []
        count = 0
        for i in string:
            if i == '0':
                if temp[-2:] == ['1','1']:
                    count += 1
                    temp.pop()
                    temp.pop()
                else:
                    temp.append(i)
                    
            else:
                temp.append(i)
        if count == 0:
            answer.append(string)
            continue
        else:
            result = []
            
            while True:
                if len(temp) == 0:
                    break
                if temp[-1] == '0':
                    break
                else:
                    result.append(temp.pop())
            
            # result = result[::-1]
            t = ['1','1','0'] * count
            result = t + result
            
            result = temp + result
            result = ''.join(result)
            answer.append(result)
            
    return answer