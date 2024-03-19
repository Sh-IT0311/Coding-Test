import sys

K, P, N = map(int, sys.stdin.readline().split())

mod = int(1e9 + 7)

def pow(x, y):
    if y == 1:
        return x

    if y % 2 == 0:
        value = 1

    else:
        y -= 1
        value = x

    temp = pow(x, y // 2)
    return value * temp * temp % mod

value = pow(P, 10 * N)
value *= K
print(value % mod)