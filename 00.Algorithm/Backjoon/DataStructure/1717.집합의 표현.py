import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

# 첫번째 시도: 메모리 초과
# 연속적으로 모든 수들이 연결되었다면 호출시 10만번
# 호출되면서 메모리+시간 초과 가능성
roots = []

def unif(a, b):
    sml, big = min(a,b), max(a,b)
    # if roots[big] != roots[sml]:
    #     roots[big] = roots[sml]
    if roots[getrt(big)] != roots[sml]:
        roots[getrt(big)] = roots[sml]

def getrt(a):
    if roots[a] == a:
        return a
    return getrt(roots[a])

def unifchk(a, b):
    # ga, gb = getrt(a), getrt(b)
    # return ga == gb
    return getrt(a) == getrt(b)

def main():
    global roots
    n, m = map(int, input().split())
    roots = [i for i in range(n+1)]
    for _ in range(m):
        func, a, b = map(int, input().split())
        if func == 0:
            unif(a, b)
        elif unifchk(a, b):
            print('YES')
        else:
            print('NO')

main()


"""

7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

3 4
0 0 1
0 2 3
0 1 2
1 0 3

3 3
0 0 1
0 2 3
1 0 3

3 4
0 0 1
0 2 3
0 1 3
1 0 2

"""