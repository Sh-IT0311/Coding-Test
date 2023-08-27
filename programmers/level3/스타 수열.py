from collections import Counter, deque, defaultdict
def solution(a):
    
    if len(a) <= 3:
        return 0
    
    n = len(a)
    temp = 0
    for i in range(1,n):
        if a[0] == a[i]:
            temp = i
        else:
            break
    a = a[temp:]
    
    n = len(a)
    temp = n - 1
    for i in range(n-2,-1,-1):
        if a[n-1] == a[i]:
            temp = i
        else:
            break       
    a = a[:temp+1]
  
    n,temp,i = len(a), a[0], 1
    interval = []
    while i < n:
        if a[i] != temp:
            temp = a[i]
            i += 1
        else:
            memo = [i-1]
            i += 1

            while True:
                if a[i] == temp:
                    i += 1
                else:
                    if i - memo[0] >= 3:
                        memo.append(i-1)
                        interval.append(memo)
                    temp = a[i]
                    i += 1
                    break
    
    interval.reverse()
    for start,end in interval:
        a = a[:start+1] + a[end:]
    n = len(a)
    value, num = max(dict(Counter(a)).items(), key = lambda x : x[1])
    #value, num = max(counter.items(), key = lambda x : x[1])
    check = [False] * n
    answer = 0
    for i in range(n):
        if check[i] == False and value == a[i]:
            if i == 0:
                if check[i+1] == False and a[i] != a[i+1]:
                    answer += 2
                    check[i],check[i+1] = True, True
            elif i == n-1:
                if check[i-1] == False and a[i] != a[i-1]:
                    answer += 2
                    check[i],check[i-1] = True, True
            else:
                if check[i-1] == False and a[i] != a[i-1]:
                    answer += 2
                    check[i],check[i-1] = True, True
                
                elif check[i+1] == False and a[i] != a[i+1]:
                    answer += 2
                    check[i],check[i+1] = True, True
                    
                

    return answer