def solution(n, t, m, timetable):
    interval = [(540 + i * t) for i in range(n)]
    groups = [0] * n
    times = list()
    
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        temp = hour * 60 + minute
        
        flag = False
        if temp <= interval[0]:
            groups[0] += 1
            times.append(temp)
            flag = True
        
        if not flag:
            for i in range(n-1):
                if interval[i] < temp <= interval[i+1]:
                    groups[i+1] += 1
                    times.append(temp)
                    break
    
    for i in range(n-1):
        if groups[i] > m:
            groups[i+1] += (groups[i] - m)
            groups[i] = m
    
    times.sort()
    if groups[-1] < m:
        hour, minute = divmod(interval[-1], 60)
        return '{:02}:{:02}'.format(hour,minute)
    
    else:
        index = groups[-1] - m + 1
        hour,minute = divmod(times[-index]-1, 60)
        return '{:02}:{:02}'.format(hour, minute)