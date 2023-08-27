def solution(n, m, x, y, queries):
    x_min, x_max, y_min, y_max = x,x,y,y
    for direction, value in reversed(queries):
        if direction == 0:
            y_max += value
            if y_max >= m:
                y_max = m-1
                
            if y_min != 0:
                y_min += value
        elif direction == 1:
            y_min -= value
            if y_min < 0:
                y_min = 0
                
            if y_max != m-1:
                y_max -= value
            
        elif direction == 2:
            x_max += value
            if x_max >= n:
                x_max = n-1
                
            if x_min != 0:
                x_min += value
        elif direction == 3:
            x_min -= value
            if x_min < 0:
                x_min = 0
                
            if x_max != n-1:
                x_max -= value

        if x_max < 0 or x_min >= n or y_max < 0 or y_min >= m:
            return 0
                 
    return (x_max - x_min + 1) * (y_max - y_min + 1)