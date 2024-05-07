import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

def find_values(scores):
    values = [scores[0]]
    temp = scores[0]
    for score in scores[1:]:
        if temp < 0:
            temp = score
        else:
            temp += score
        values.append(max(values[-1], temp))
    return values

current_values = find_values(scores)
scores.reverse()
reverse_values = find_values(scores)
reverse_values.reverse()

result = float('-inf')
for i in range(n-2):
    result = max(result, current_values[i] + reverse_values[i+2])
print(result)