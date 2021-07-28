import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
mapp = []
for _ in range(R):
    # mapp.append(list(map(lambda x: ord(x)-65, input().strip())))
    mapp.append(list(input().strip()))

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]
# answer = 1
# # alp_vstd = {chr(ord('A')+alp): False for alp in range(26)}
# alp_vstd = [False] * 26
# alp_vstd[mapp[0][0]] = True

# def dfs(x, y, now):
#     global answer
#     answer = max(answer, now)
#     for dir in range(4):
#         new_x = x + dx[dir]
#         new_y = y + dy[dir]
#         if 0 <= new_x < R and 0 <= new_y < C\
#             and not alp_vstd[mapp[new_x][new_y]]:
#             alp_vstd[mapp[new_x][new_y]] = True
#             dfs(new_x, new_y, now+1)
#             alp_vstd[mapp[new_x][new_y]] = False



dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
answer = 1
# que = deque([(0,0,mapp[0][0])])
que = set([(0,0,mapp[0][0])])
def bfs():
    global answer
    while que:
        # x, y, now_path_str = que.popleft()
        x, y, now_path_str = que.pop()
        for dir in range(4):
            new_x = x + dx[dir]
            new_y = y + dy[dir]
            if 0 <= new_x < R and 0 <= new_y < C\
                and mapp[new_x][new_y] not in now_path_str:
                # que.append((new_x, new_y, now_path_str + mapp[new_x][new_y]))
                que.add((new_x, new_y, now_path_str + mapp[new_x][new_y]))
                answer = max(answer, len(now_path_str)+1)


# dfs(0,0,1)
bfs()
print(answer)

"""

2 4
CAAB
ADCB

3 6
HFDFFB
AJHGDH
DGAGEH

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH

12 16
ABCDEFGHIJKLMNOP
BCDEFGHIJKLMNOPQ
CDEFGHIJKLMNOPQR
DEFGHIJKLMNOPQRS
EFGHIJKLMNOPQRST
FGHIJKLMNOPQRSTU
GHIJKLMNOPQRSTUV
HIJKLMNOPQRSTUVW
IJKLMNOPQRSTUVWX
JKLMNOPQRSTUVWXY
KLMNOPQRSTUVWXYZ
LMNOPQRSTUVWXYZA

"""