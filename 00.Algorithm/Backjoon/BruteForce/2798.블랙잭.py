n,m = map(int, input().split())

soo_list = list(map(int, input().split()))
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = soo_list[i] + soo_list[j] + soo_list[k]
            if tmp <= m:
                answer = max(answer, tmp)

print(answer)

"""
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295
"""