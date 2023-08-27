from collections import defaultdict

def solution(words):
    answer = 0
    
    data = defaultdict(list)
    for word in words:
        data[word[0]].append(word)
        
    while True:
        keys = list()
        deletes = list()
        
        for key, values in data.items():
            if len(values) != 1:
                keys.append(key)
            else:
                deletes.append(key)
        
        for delete in deletes:
            data.pop(delete)
            answer += len(delete)
            
        if len(keys) == 0:
            break
            
        for key in keys:
            values = data.pop(key)
            num = len(key) + 1
            for value in values:
                data[value[:num]].append(value)

    return answer