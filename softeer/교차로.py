import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N = int(input().rstrip())
cars = list()

for _ in range(N):
    cars.append(input().rstrip().split())

def solution(N, cars):
    answer = [-1] * N
    
    q = [deque() for _ in range(4)]
    q += [q[0]]
    nq = 0
    
    adict = {'A' : 0, 'B' : 3, 'C' : 2, 'D' : 1}
    orders = deque()
    for i in range(N):
        t,w = cars[i]
        t = int(t)
        orders.append((t, adict[w], i))

    times = 0
    while orders or nq:
        if nq == 0:
            times = orders[0][0]
            while orders:
                if orders[0][0] <= times:
                    time, what, idx = orders.popleft()
                    nq += 1
                    q[what].append(idx)
                else:
                    break 
                             
        else:
            now = list()
            for i in range(4):
                if q[i] and not q[i+1]:
                    now.append(i)
            
            if now:
                for i in now:
                    answer[q[i].popleft()] = times
                    nq -= 1
            else:
                break
   
            times += 1
            while orders:
                if orders[0][0] <= times:
                    time, what, idx = orders.popleft()
                    nq += 1
                    q[what].append(idx)
                else:
                    break
    return answer

results = solution(N, cars)
for result in results:
    print(result)