from heapq import heappush, heappop, heapify

def solution(n, k, cmd):
    upper = list(map(lambda x : -x, range(k)))
    heapify(upper)
    
    bottom = list(range(k,n))
    heapify(bottom)
    backup = list()
    for c in cmd:
        if len(c) == 1:
            if c == 'Z':
                value = backup.pop()

                if bottom[0] <= value:
                    heappush(bottom, value)
                else:
                    heappush(upper, -value)
            elif c == 'C':
                backup.append(heappop(bottom))
                if not bottom:
                    heappush(bottom, -heappop(upper))
        else:
            oper, value = c.split()
            value = int(value)
            if oper == 'D':
                for _ in range(value):
                    heappush(upper, -heappop(bottom))
            elif oper == 'U':
                for _ in range(value):
                    heappush(bottom, -heappop(upper))
                    
    answer = ['X'] * n

    for d in bottom:
        answer[d] = 'O'
        
    for u in upper:
        answer[-u] = 'O'

    return ''.join(answer)