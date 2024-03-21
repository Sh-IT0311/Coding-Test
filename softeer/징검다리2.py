import sys
input = sys.stdin.readline
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

def make_history(arr):
    sequence = [arr[0]]
    history = [(arr[0], 1)]
    for i in range(1, N):
        if sequence[-1] < arr[i]:
            sequence.append(arr[i])
    
        else:
            sequence[bisect_left(sequence, arr[i])] = arr[i]
        
        history.append((sequence[-1], len(sequence)))
    return history

current_history = make_history(A)
A.reverse()
reverse_history = make_history(A)
reverse_history.reverse()

result = 1
for i in range(N-1):
    _prev = current_history[i]
    _next = reverse_history[i+1]

    if _prev[0] > _next[0]:
        result = max(result, _prev[1] + _next[1])
print(result)