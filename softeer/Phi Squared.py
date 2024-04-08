import sys
input = sys.stdin.readline

N = int(input())
data = list(zip(range(1, N+1), map(int, input().split()))) + [(N+1, 0)]
stack = [(0, 0)]

while len(data) > 2:
    index = 0
    while index < len(data)-1:
        li, lv = stack.pop()
        mi, mv = data[index]
        ri, rv = data[index+1]

        if lv <= mv and rv <= mv:
            stack.append((mi, mv + lv + rv))
            index += 1
        else:
            if lv <= mv:
                stack.append((mi, mv + lv))
            elif rv <= mv:
                stack.append((li, lv))
                stack.append((mi, mv + rv))
                index += 1
            else:
                stack.append((li, lv))
                stack.append((mi, mv))
        index += 1

    data = stack + [(N+1, 0)]
    stack = [(0, 0)]

index, value = data[0]
print(value)
print(index)