def solution(arrows):
    answer = 0
    points = {(0,0)}
    lines = set()
    
    dx = (-1,-1,0,1,1,1,0,-1)
    dy = (0,1,1,1,0,-1,-1,-1)
    
    x, y = 0, 0
    for arrow in arrows:
        sx = x + dx[arrow]
        sy = y + dy[arrow]
        nx = x + dx[arrow] * 2
        ny = y + dy[arrow] * 2
        
        line1 = tuple(sorted(((x,y), (sx,sy))))
        line2 = tuple(sorted(((sx,sy), (nx,ny))))
        
        if (sx,sy) in points: # small1 만들어지나?
            if not line1 in lines:
                answer += 1
            
        if (nx,ny) in points: # big or small2 decision
            if not line2 in lines:
                answer += 1
                   
        lines.add(line1)
        lines.add(line2)
        points.add((nx,ny))
        points.add((sx,sy))
        x,y = nx, ny
    
    return answer