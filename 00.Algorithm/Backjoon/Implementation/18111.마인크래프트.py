import sys
input = sys.stdin.readline
n,m,b = map(int, input().split())

num_cnt = {}
for _ in range(n):
    tmp = list(map(int, input().split()))
    for i in tmp:
        if i not in num_cnt:
            num_cnt[i] = 0
        num_cnt[i] += 1

num_cnt = dict(sorted(num_cnt.items(), key=lambda x:x[0]))
range_min, range_max = min(num_cnt.keys()), max(num_cnt.keys())
answer = (int(1e9), 0)
for i in range(range_min, range_max+1):
    time_sum, invt = 0, b
    for j in num_cnt:
        if i == j:
            continue
        work = abs(i-j) * num_cnt[j]
        if i > j:
            time_sum += work
            invt -= work
        else:
            time_sum += work * 2
            invt += work
    
    if invt >= 0 and time_sum <= answer[0]:
        answer = (time_sum, i)

print(answer[0], answer[1])

# 틀린 곳을 찾기 힘들어 타인블로그 참조해보니 똑같이 딕셔너리로 땅 높이 별 개수 저장 후
# 깎고 쌓는 작업을 재고 확인하며 시간 측정 후 정답 갱신하는 식으로 했는데 왜 채점 1프로 부터
# 바로 틀렸다고 하는지 모르겠네
# 하 출력문제였다!

"""

1 3 99
0 0 1

3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

3 4 1
64 64 64 64
64 64 64 64
64 64 64 63

3 4 0
64 64 64 64
64 64 64 64
64 64 64 63

1 3 0
0 1 0

1 3 2
0 1 0

1 6 2
1 2 2 3 3 3

1 3 0
1 4 1

"""