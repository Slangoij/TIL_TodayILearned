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