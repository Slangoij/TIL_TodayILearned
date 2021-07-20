R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(list(map(int, input().split())))

dp = []
for i in range(R):
    for j in range(C):
        now_soo = maps[i][j]
        if now_soo