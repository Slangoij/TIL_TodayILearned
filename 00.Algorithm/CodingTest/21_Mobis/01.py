from itertools import product,permutations

def solution(dice):
    answer = 0
    chk = [False] * 10000
    dicidx = [i for i in range(len(dice))]
    idx = [i for i in range(6)]
    for i in range(len(dice)):
        for diccombi in permutations(dicidx, i+1):
            for combi in product(idx, repeat=i+1):
                strnums = ''
                for j in range(i+1):
                    strnums += str(dice[diccombi[j]][combi[j]])
                chk[int(strnums)] = True
    for i in range(1,10000):
        if not chk[i]:
            answer = i
            break
    return answer

dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]

print(solution(dice))