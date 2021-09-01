T = int(input())
if T % 10:
    print(-1)
else:
    but = [300,60,10]
    for i in range(3):
        cnt = T//but[i]
        print(cnt, end=' ')
        T -= cnt * but[i]