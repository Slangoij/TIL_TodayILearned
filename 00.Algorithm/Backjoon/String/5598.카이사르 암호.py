import sys
input = sys.stdin.readline

cha_set = {chr(bf+ord('A')):chr(ord('A')+(bf-3)%26) for bf in range(26)}
bf_k = input().strip()
answer = ''
for i in bf_k:
    answer += cha_set[i]

print(answer)

"""

MRL

FURDWLD

"""