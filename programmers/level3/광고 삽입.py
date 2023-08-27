def solution(play_time, adv_time, logs):
    h,m,s = tuple(map(int,play_time.split(':')))
    total = h * 3600 + m * 60 + s
    data = [0] * total
    l = len(logs)
    starts = list()
    ends = list()
    
    for log in logs:
        start, end = log.split('-')
        sh, sm, ss = tuple(map(int, start.split(':')))
        eh, em, es = tuple(map(int, end.split(':')))
        
        starts.append(sh * 3600 + sm * 60 + ss)
        ends.append(eh * 3600 + em * 60 + es)
        
    starts.sort()
    ends.sort()
    
    si = 1
    ei = 0
    now = starts[0]
    num = 1
    
    while si <= l-1:
        if starts[si] < ends[ei]:
            for index in range(now, starts[si]):
                data[index] = num
            now = starts[si]
            
            num += 1
            si += 1
            
        elif starts[si] == ends[ei]:
            for index in range(now, starts[si]):
                data[index] = num
            now = starts[si]
            
            si += 1
            ei += 1
        else:
            for index in range(now, ends[ei]):
                data[index] = num
            now = ends[ei]
            
            num -= 1
            ei += 1
    
    while ei <= l-1:
        for index in range(now, ends[ei]):
            data[index] = num    
        now = ends[ei]
        
        num -= 1
        ei += 1
            
    h,m,s = tuple(map(int,adv_time.split(':')))
    adv = h * 3600 + m * 60 + s
    value = sum(data[:adv])
    max_value = value
    max_index = adv - 1
    
    for index in range(adv, total):
        value = value + data[index] - data[index - adv]
        if max_value < value:
            max_value = value
            max_index = index
    
    max_index -= (adv - 1)
    h = max_index // 3600
    max_index -= h * 3600
    m = max_index // 60
    max_index -= m * 60
        
    return '{:02}:{:02}:{:02}'.format(h,m,max_index)