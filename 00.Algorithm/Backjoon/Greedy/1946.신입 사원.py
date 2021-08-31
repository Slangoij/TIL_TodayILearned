import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    rates = []
    for _ in range(N):
        rates.append(list(map(int, input().split())))
    rates.sort(key=lambda x: x[0])
    
    ans = 1
    intv = list(zip(*rates))[1]
    minval = intv[0]
    for i in range(1,N):
        if intv[i] < minval:
            minval = intv[i]
            ans += 1

    print(ans)

"""

2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

1
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

"""