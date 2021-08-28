K = int(input())
mapp = []
for _ in range(6):
    mapp.append(list(map(int,input().split())))

dirs = [[] for _ in range(5)]
little = []
for j in range(6):
    cnt = 0
    chk = False
    for i in range(6):
        if mapp[(j+i)%6][0] == mapp[(j+i+2)%6][0]:
            cnt += 1
            if cnt == 2:
                little.append(mapp[(j+i)%6][1])
                little.append(mapp[(j+i+1)%6][1])
                chk = True
                break
    dirs[mapp[j][0]].append(mapp[j][1])

area = max(dirs[1]+dirs[2])*max(dirs[3]+dirs[4])-little[0]*little[1]

print(area*K)


"""

7
3 20
1 100
4 50
2 160
3 30
1 60

"""