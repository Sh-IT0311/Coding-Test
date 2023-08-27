from math import ceil

def solution(n, stations, w):
    answer = 0
    
    s = len(stations)
    section = list()
    value = w * 2 + 1
    
    for station in stations:
        section.append((station - w, station + w))

    temp = section[0][0] - 1
    if temp >= 1:
        answer += ceil(temp / value)
    for i in range(s-1):
        temp = section[i+1][0] - section[i][1] -1
        if temp >= 1:
            answer += ceil(temp / value)
    temp = n - section[-1][1]
    if temp >= 1:
        answer += ceil(temp / value)
    
    return answer