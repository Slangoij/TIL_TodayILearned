import sys
input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d_sq = (x1-x2)**2 + (y1-y2)**2
    if d_sq == 0:
        if r1 == r2:
            answer.append(-1)
        else:
            answer.append(0)
        continue
    if (r1 - r2)**2 < d_sq < (r1 + r2)**2:
        answer.append(2)
    elif d_sq == (r1 - r2)**2 or d_sq == (r1 + r2)**2:
        answer.append(1)
    else:
        answer.append(0)

for ans in answer:
    print(ans)

# # 첫번째 시도: d를 구할 때 제곱근을 씌우는 데서 오차가 발생해서 계속 오류
# d = int(((x1-x2)**2 + (y1-y2)**2)**(1/2))
# if d == 0:
#     if r1 == r2:
#         answer.append(-1)
#     else:
#         answer.append(0)
#     continue
# if abs(r1 - r2) < d < r1 + r2:
#     answer.append(2)
# elif d == abs(r1 - r2) or d == r1 + r2:
#     answer.append(1)
# else:
#     answer.append(0)
"""

3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5

"""