def solution(sequence):
    n = len(sequence)
    data = [0] * n
    data[0] = sequence[0]
    temp = -1
    _min = data[0]
    _min_index = 0
    _max = data[0]
    _max_index = 0
    for i in range(1,n):
        seq = sequence[i]
        data[i] = seq * temp + data[i-1]
        temp = -temp
        
        if _min > data[i]:
            _min = data[i]
            _min_index = i
            
        if data[i] > _max:
            _max = data[i]
            _max_index = i

    answer = max(_max, -_min)
    
    if _max_index > 0:
        temp = min(data[:_max_index])
        if temp < 0:
            answer = max(answer, _max - temp)
    
    if _min_index > 0:
        temp = max(data[:_min_index])
        if temp > 0:
            answer = max(answer, -_min + temp)
            
    return answer