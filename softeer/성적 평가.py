import sys
input = sys.stdin.readline

N = int(input())

score1 = list()
score2 = list()
score3 = list()
temp = [0] * N

for s1, i in zip(map(int, input().split()), range(N)):
    score1.append((s1, i))
    temp[i] += s1

for s2, i in zip(map(int, input().split()), range(N)):
    score2.append((s2, i))
    temp[i] += s2

for s3, i in zip(map(int, input().split()), range(N)):
    score3.append((s3, i))
    temp[i] += s3

total = [(temp[i], i) for i in range(N)]

score1.sort(reverse = True)
score2.sort(reverse = True)
score3.sort(reverse = True)
total.sort(reverse = True)

grade1 = [0] * N
grade2 = [0] * N
grade3 = [0] * N
result = [0] * N

def set_grade(slist, glist):
    grade = 1
    prev, index = slist[0]
    glist[index] = grade
    for i in range(1, N):
        now, index = slist[i]

        if now != prev:
            grade = i+1
        
        prev = now
        glist[index] = grade

    return

set_grade(score1, grade1)
set_grade(score2, grade2)
set_grade(score3, grade3)
set_grade(total, result)

print(" ".join(map(str, grade1)))
print(" ".join(map(str, grade2)))
print(" ".join(map(str, grade3)))
print(" ".join(map(str, result)))