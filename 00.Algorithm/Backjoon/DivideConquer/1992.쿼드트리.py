import sys
import math
input = sys.stdin.readline

N = int(input())
for_sum = []
mapp = []
for _ in range(N):
    tmp = input().strip()
    for_sum.append(list(map(int, list(tmp))))
    mapp.append(tmp)

def chkall(x,y,leng):
    summ = 0
    for i in range(x, x+leng):
        summ += sum(for_sum[i][y:y+leng])
    if summ == 0 or summ == leng**2:
        return True
    return False

        
def dfs(x,y,leng):
    if chkall(x,y,leng):
        return mapp[x][y]

    leng = leng//2

    return '(' + dfs(x,y,leng) + dfs(x,y+leng,leng) + dfs(x+leng,y,leng) + dfs(x+leng,y+leng,leng) + ')'


print(dfs(0,0,N))

"""

8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

"""

# # 첫번째 풀이
# # 무조건 반으로 나누고 시작했다가 한참 고민하고
# # dfs처음부터 다시 시작하고 시뮬레이션을 돌리니 처음에 전체 확인하고 차근차근 들어가는게 나았다.
# answer = ''
# def dfs(x,y,leng):
#     global answer

#     if chkall(x,y,leng) and chkall(x,y+leng,leng)\
#         and chkall(x+leng,y,leng) and chkall(x+leng,y+leng,leng):
#         if leng == 1:
#             return '('+ mapp[x][y] + mapp[x][y+1] + mapp[x+1][y] + mapp[x+1][y+1] + ')'
#         return mapp[x][y]
    
#     leng = leng//2
#     return '(' + dfs(x,y,leng) + dfs(x,y+leng,leng) + dfs(x+leng,y,leng) + dfs(x+leng,y+leng,leng) + ')'