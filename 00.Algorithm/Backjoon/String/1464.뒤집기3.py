S = input()

if len(S) <= 2:
    print(min(S, "".join(reversed(S))))
else:
    answer = S[:2]
    for i in range(1,len(S)-1):
        if (answer[-1] == min(answer) and S[i+1] > min(answer)) or\
            (answer[0] == min(answer) and S[i+1] <= min(answer)):
            answer = "".join(reversed(answer))
        answer += S[i+1]

    print(min(answer, "".join(reversed(answer))))

"""

BCDAF



"""
# 1차 시도: 적은 길이 문자열 예시를 miss
# S = input()
from itertools import permutations

def func(S):
    answer = S[:2]
    for i in range(1,len(S)-1):
        # S = min(S[:i], "".join(reversed(S[:i]))) + S[i:]
        if answer[-1] == min(answer)\
            or (answer[0] == min(answer) and S[i+1] < min(answer)):
            answer = "".join(reversed(answer))
        answer += S[i+1]

    print(min(answer, "".join(reversed(answer))))


permutations(list(map()))
