from collections import defaultdict
from heapq import heappush,heappop

def solution(genres, plays):
    answer = []
    genre_sum = defaultdict(int)
    genre_order = defaultdict(list)
    
    total = len(genres)
    for i in range(total):
        genre_sum[genres[i]] += plays[i]
        heappush(genre_order[genres[i]], (-plays[i],i))
        
    genre_sum = sorted(genre_sum.items(), reverse = True, key = lambda x : x[1])
    
    for a,b in genre_sum:
        temp = heappop(genre_order[a])
        answer.append(temp[1])
        if len(genre_order[a]) != 0:
            temp = heappop(genre_order[a])
            answer.append(temp[1])
    return answer