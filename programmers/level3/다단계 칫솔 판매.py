from collections import defaultdict,deque

def solution(enroll, referral, seller, amount):
    n = len(enroll)
    
    mydict = dict()
    
    for i in range(n):
        mydict[enroll[i]] = referral[i]
        
    result = defaultdict(int)
    
    for i in range(len(seller)):
        key,value = seller[i], amount[i]*100
        while True:
            temp = value // 10
            result[key] += (value - temp)
            
            key = mydict[key]
            value = temp
            
            if key == '-' or value == 0:
                break

    return [result[who] for who in enroll]