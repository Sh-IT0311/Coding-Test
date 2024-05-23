import sys
input = sys.stdin.readline
K, P, N = map(int, input().split())
R = 1000000007

def recursive_value(P, N, R):
    if N == 1:
        return P % R
    else:
        value = recursive_value(P, N // 2, R)
        if N % 2 == 0:
            return (value * value) % R
        else:
            return (value * value * P) % R

result = (K * recursive_value(P, N, R)) % R
print(result)