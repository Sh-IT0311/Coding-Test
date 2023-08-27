from collections import deque

def solution(m, n, puddles):
    graph = [[0] * m for _ in range(n)]
    
    for i in range(m):
        graph[0][i] = 1
    for i in range(n):
        graph[i][0] = 1
        
    for q,w in puddles:
        graph[w-1][q-1] = -1
        if w-1 == 0:
            for i in range(q,m):
                graph[0][i] = 0
        elif q-1 == 0:
            for i in range(w,n):
                graph[i][0] = 0
        
    for i in range(1,n):
        for j in range(1,m):
            if graph[i][j] == - 1:
                pass
            else:
                if graph[i-1][j] == -1:
                    graph[i][j] = graph[i][j-1]
                elif graph[i][j-1] == - 1:
                    graph[i][j] = graph[i-1][j]
                else:
                    graph[i][j] = graph[i-1][j] + graph[i][j-1]
        

    return graph[n-1][m-1] % 1000000007