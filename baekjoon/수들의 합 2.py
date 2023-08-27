n,m = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
data.insert(0,0)
n += 1
acc = [0] * n
for i in range(1,n):
    acc[i] = data[i] + acc[i-1]

for i in range(1,n):
    for j in range(i, n):
        if acc[j] - acc[i-1] == m:
            answer += 1
            break
            
        elif acc[j] - acc[i-1] > m:
            break
            

print(answer)