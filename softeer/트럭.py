import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
data = defaultdict(int)
for _ in range(N):
    num, *users = map(int, input().split())
    temp = list()
    for i in range(0, num*2, 2):
        temp.append((users[i], users[i+1]))
    temp.sort()
    max_value = 0
    for t, m in temp:
        prev = max_value
        max_value = max(m, max_value)
        data[t] += (max_value - prev)

M = int(input())
Q = list(map(int, input().split()))

def solution(data, Q):
    answer = dict()

    keys = list(data.keys())
    k = len(keys)
    keys.sort()

    result = dict()
    result[keys[0]] = data[keys[0]]
    for i in range(1,k):
        result[keys[i]] = data[keys[i]] + result[keys[i-1]]

    temp = Q.copy()
    temp.sort()

    idx = 0
    for target in temp:
        if target <= result[keys[0]]:
            answer[target] = keys[0]
        
        elif target > result[keys[-1]]:
            answer[target] = -1

        else:
            while idx < k-1:
                if result[keys[idx]] < target <= result[keys[idx+1]]:
                    answer[target] = keys[idx+1]
                    break
                idx += 1

    return answer

result = solution(data, Q)
print(' '.join([str(result[i]) for i in Q]))