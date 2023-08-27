def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    n = len(A)
    j = 0
    
    for i in range(n):
        if A[j] < B[i]:
            answer += 1
            j += 1
    
    return answer