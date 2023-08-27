def solution(N, number):
    data = [set() for _ in range(9)]
    
    temp = 0
    for num in range(1,9):
        temp = temp * 10 + N
        data[num].add(temp)
        
        for half in range(1, num // 2 + 1):
            for x in data[half]:
                for y in data[num - half]:
                    data[num].add(x + y)
                    data[num].add(x - y)
                    data[num].add(y - x)
                    data[num].add(x * y)
                    if x != 0:
                        data[num].add(y // x)
                    if y != 0:
                        data[num].add(x // y)
        if number in data[num]:
            return num
                        
    return -1