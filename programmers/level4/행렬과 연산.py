from collections import deque

def solution(rc, operations):
    rows = len(rc)
    columns = len(rc[0])
    
    left = deque()
    middle = deque()
    right = deque()
    
    for i in range(rows):
        left.append(rc[i][0])
        middle.append(deque(rc[i][1:-1]))
        right.append(rc[i][-1])

    for operation in operations:
        if operation[0] == 'R':
            middle[0].appendleft(left.popleft())
            right.appendleft(middle[0].pop())
            middle[-1].append(right.pop())
            left.append(middle[-1].popleft())
        
        elif operation[0] == 'S':
            left.appendleft(left.pop())
            middle.appendleft(middle.pop())
            right.appendleft(right.pop())
    
    
    answer = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if j == 0:
                answer[i][j] = left[i]
            elif j == columns -1:
                answer[i][j] = right[i]
            else:
                answer[i][j] = middle[i][j-1]
    
    return answer