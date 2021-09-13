# 두번째 시도:
# 이와 같이 양쪽의 포함 원소수를 비교하고 적은 것을 많은 것
# 기준으로 바꾸면 루트를 찾아갈 필요없이 바로 roots배열에서 값 확인만 하면 된다.
# 가 아니라 기존의 부모형태로 찾는 것이 맞다.
# 함수에 매개변수로 리스트나 자료구조를 넣어주면 레퍼런스 참조와 비슷한 효과
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def getrt(rts, a):
    if rts[a] < 0:    
        return a
    rts[a] = getrt(rts, rts[a])
    return rts[a]

def unif(rts, a, b):
    a = getrt(rts, a)
    b = getrt(rts, b)
    # rts[max(a, b)] = min(a, b)
    if a != b:
        if rts[a] < rts[b]:
            rts[a] += rts[b]
            rts[b] = a
        else:
            rts[b] += rts[a]
            rts[a] = b

n, m = map(int, input().split())
rts = [-1 for i in range(n+1)]
for _ in range(m):
    func, a, b = map(int, input().split())
    if func == 0:
        unif(rts, a, b)
    else:
        if getrt(rts, a) == getrt(rts, b):
            print('YES')
        else:
            print('NO')


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

# # 첫번째 시도: 메모리 초과
# # 연속적으로 모든 수들이 연결되었다면 호출시 10만번
# # 호출되면서 메모리+시간 초과 가능성
# roots = []

# def unif(a, b):
#     sml, big = min(a,b), max(a,b)
#     # if roots[big] != roots[sml]:
#     #     roots[big] = roots[sml]
#     if roots[getrt(big)] != roots[sml]:
#         roots[getrt(big)] = roots[sml]

# def getrt(a):
#     if roots[a] == a:
#         return a
#     return getrt(roots[a])

# def unifchk(a, b):
#     # ga, gb = getrt(a), getrt(b)
#     # return ga == gb
#     return getrt(a) == getrt(b)

# def main():
#     global roots
#     n, m = map(int, input().split())
#     roots = [i for i in range(n+1)]
#     for _ in range(m):
#         func, a, b = map(int, input().split())
#         if func == 0:
#             unif(a, b)
#         elif unifchk(a, b):
#             print('YES')
#         else:
#             print('NO')

# main()