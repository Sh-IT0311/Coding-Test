from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    
    original = defaultdict(list)
    reverse = defaultdict(list)
    
    for word in words:
        original[len(word)].append(word)
        reverse[len(word)].append(word[::-1])
        
    for key in original.keys():
        original[key].sort()
        reverse[key].sort()
        
    for query in queries:
        data = original[len(query)]
        if query[0] == '?':
            query = query[::-1]
            data = reverse[len(query)]
        
        answer.append(bisect_right(data, query.replace('?','z')) - bisect_left(data, query.replace('?','a')))
    return answer