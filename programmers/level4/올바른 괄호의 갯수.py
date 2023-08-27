from math import factorial

def solution(n):
    return factorial(2 * n) // factorial(n) // factorial(n+1)