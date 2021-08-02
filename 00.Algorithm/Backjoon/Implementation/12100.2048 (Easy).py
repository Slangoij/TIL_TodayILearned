import sys
input = sys.stdin.readline

N = int(input())
mapp = []
for _ in range(N):

    mapp.append(list(map(int, input().split())))

def mvup():
    global mapp
    lines = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mapp[i][j]:
                lines[j].append(mapp[i][j])

    mapp = [[0]*N for _ in range(N)]
    for i in range(N):
        cnt, j = 0, 0
        while cnt < len(lines[i])-1:
            if lines[i][cnt] == lines[i][cnt+1]:
                mapp[j][i] = lines[i][cnt]*2
                cnt += 1
            else:
                mapp[j][i] = lines[i][cnt]
            cnt += 1
            j += 1
        if cnt == len(lines[i])-1:
            mapp[j][i] = lines[i][cnt]

def mvdown():
    global mapp
    lines = [[] for _ in range(N)]
    for i in range(N-1,-1,-1):
        for j in range(N):
            if mapp[i][j]:
                lines[j].append(mapp[i][j])

    mapp = [[0]*N for _ in range(N)]
    for i in range(N):
        cnt, j = 0, 0
        while cnt < len(lines[i])-1:
            if lines[i][cnt] == lines[i][cnt+1]:
                mapp[N-1-j][i] = lines[i][cnt]*2
                cnt += 1
            else:
                mapp[N-1-j][i] = lines[i][cnt]
            cnt += 1
            j += 1
        if cnt == len(lines[i])-1:
            mapp[N-1-j][i] = lines[i][cnt]
    
def mvleft():
    global mapp
    lines = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if mapp[i][j]:
                lines[i].append(mapp[i][j])

    mapp = [[0]*N for _ in range(N)]
    for i in range(N):
        cnt, j = 0, 0
        while cnt < len(lines[i])-1:
            if lines[i][cnt] == lines[i][cnt+1]:
                mapp[i][j] = lines[i][cnt]*2
                cnt += 1
            else:
                mapp[i][j] = lines[i][cnt]
            cnt += 1
            j += 1
        if cnt == len(lines[i])-1:
            mapp[i][j] = lines[i][cnt]
            
def mvright():
    global mapp
    lines = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-1,-1,-1):
            if mapp[i][j]:
                lines[i].append(mapp[i][j])

    mapp = [[0]*N for _ in range(N)]
    for i in range(N):
        cnt, j = 0, 0
        while cnt < len(lines[i])-1:
            if lines[i][cnt] == lines[i][cnt+1]:
                mapp[i][N-1-j] = lines[i][cnt]*2
                cnt += 1
            else:
                mapp[i][N-1-j] = lines[i][cnt]
            cnt += 1
            j += 1
        if cnt == len(lines[i])-1:
            mapp[i][N-1-j] = lines[i][cnt]

answer = 0
def dfs(now):
    global answer
    if now == 5:
        for i in range(N):
            answer = max(answer, max(mapp[i]))
        return

    mvup()
    dfs(now+1)
    mvdown()
    dfs(now+1)
    mvleft()
    dfs(now+1)
    mvright()
    dfs(now+1)

dfs(0)
print(answer)

"""

3
2 2 2
4 4 4
8 8 8

"""