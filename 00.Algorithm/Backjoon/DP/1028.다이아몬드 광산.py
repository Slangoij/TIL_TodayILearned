def solution():
    R, C = map(int, input().split())
    maps = []
    for _ in range(R):
        maps.append(list(map(int, list(input()))))
        
    tmp_ret = 0
    for mapp in maps:
        tmp_ret += sum(mapp)
    if tmp_ret == 0:
        print(0)
        return False

    dp = [[[0,0] for _ in range(C)] for _ in range(R)] # 좌상, 우상 [0,0]
    # 위에서 아래로 연결길이 체크
    for i in range(1, R):
        for j in range(C):
            if maps[i][j]:
                if j > 0 and maps[i-1][j-1]:
                    dp[i][j][0] = dp[i-1][j-1][0] + 1
                if j < C-1 and maps[i-1][j+1]:
                    dp[i][j][1] = dp[i-1][j+1][1] + 1

    answer = 0
    for i in range(R-1, 1, -1):
        for j in range(C):
            if dp[i][j][0] and dp[i][j][1]:
                now_len = min(dp[i][j][0], dp[i][j][1])
                for tmp_len in range(1, now_len+1):
                    if dp[i-tmp_len][j-tmp_len][1] >= tmp_len and dp[i-tmp_len][j+tmp_len][0] >= tmp_len:
                        answer = max(answer, tmp_len)

    print(answer+1)

solution()

"""
5 5
01100
01011
11111
01111
11111

4 4
0101
1010
0101
1010

4 4
0010
0101
0010
0000

3 5
10101
01010
10101
"""