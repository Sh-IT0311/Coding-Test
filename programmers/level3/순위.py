def solution(n, results):
    INF = int(1e9)
    
    answer = 0
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for a,b in results:
        graph[b][a] = 1
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])
                
    for i in range(1,n+1):
        result = 0
        for j in range(1,n+1):
            if graph[i][j] != INF or graph[j][i] != INF:
                result +=1
        if result == n:
            answer += 1
            
    return answer