import sys
input = sys.stdin.readline

n = int(input())
ans_str = list(input().strip())
for _ in range(1,n):
    crnt_str = list(input().strip())
    for i in range(len(crnt_str)):
        if ans_str[i] != crnt_str[i]:
            ans_str[i] = '?'
print("".join(ans_str))