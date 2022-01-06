import sys
input =

def row_or(alin, blin):
    return tmplin

if __name__ == "__main__":
    mapp = []
    n = int(input())
    for _ in range(n):
        mapp.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if mapp[i][j]:
                mapp[i] = row_or(mapp[i], mapp[j])