n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for i in range(n):
    ans += A[i]*B[i]
print(ans)
