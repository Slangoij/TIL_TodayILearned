n = int(input())
lst = sorted(list(map(int, input().split())))
summ = 0
for i in range(n):
    if lst[i] > summ+1:
        break
    summ += lst[i]

print(summ+1)
