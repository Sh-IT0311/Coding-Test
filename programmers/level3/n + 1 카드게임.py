from bisect import bisect_left
from collections import deque

def solution(coin, cards):
    answer = 0
    
    n = len(cards)
    
    INIT = n // 3
    HALF = n // 2
    
    data = cards[:INIT]
    data.sort()
    
    plus = set(cards[INIT:])
    cards = deque(cards[INIT:])
    completed = set()
    
    for card in data:
        if card <= HALF:
            idx = bisect_left(data, n + 1 - card)
            
            if idx < len(data) and data[idx] + card == n + 1:
                answer += 1
                completed.add(card)
    
    for _ in range(answer * 2):
        card = cards.popleft()
        idx = bisect_left(data, card)
        data = data[:idx] + [card] + data[idx:]
    
    while coin and cards:
        for _ in range(2):
            card = cards.popleft()
            idx = bisect_left(data, card)
            data = data[:idx] + [card] + data[idx:]
        
        temp = list()
        
        for card in data:
            if card <= HALF:
                if card in completed:
                    continue
                    
                idx = bisect_left(data, n + 1 - card)
            
                if idx < len(data) and data[idx] + card == n + 1:
                    if int(data[idx] in plus) + int(card in plus) == 1:
                        answer += 1
                        coin -= 1
                        completed.add(card)
                        break
                    else:
                        temp.append(card)
                        
        else:
            if temp and coin > 1:
                coin -= 2
                answer += 1
                completed.add(temp.pop())
            else:
                break
    
    return answer + 1