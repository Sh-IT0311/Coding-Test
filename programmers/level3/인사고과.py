def solution(scores):
    temp = scores[0]
    value = temp[0] + temp[1]
    scores = list(filter(lambda x : x[0] + x[1] > value, scores))
    if not scores:
        return 1
    _max = max(scores, key = lambda x : x[0])[0]
    _max = max(_max, temp[0])
    
    data = [-1] * (_max+2)
    for a,b in scores:
        data[a] = max(data[a], b)
    for i in range(_max-1, -1, -1):
        data[i] = max(data[i], data[i+1])

    if data[temp[0]+1] > temp[1]:
        return -1

    answer = 1
    for score in scores:
        if data[score[0]+1] > score[1]:
            continue
        answer += 1
    
    return answer