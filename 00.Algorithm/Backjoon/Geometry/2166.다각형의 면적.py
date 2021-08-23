import sys
input = sys.stdin.readline

n = int(input())
x,y = [], []
for _ in range(n):
    tx, ty = map(int,input().split())
    x.append(tx)
    y.append(ty)

answer = 0
for i in range(n-1):
    answer += x[i]*y[i+1] - x[i+1]*y[i]
answer += x[n-1]*y[0] - x[0]*y[n-1]
# answer = round(abs(answer/2),1) round는 반올림시 되도록 짝수에 맞춰준다.
answer *= 5
answer = int(answer) + (1 if answer-int(answer) >= 0.5 else 0)
answer /= 10

print(abs(answer))