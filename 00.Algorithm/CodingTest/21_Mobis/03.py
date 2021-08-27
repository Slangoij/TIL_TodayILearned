
from math import log2

def sol(nums):
    maxx = max(nums)
    ans = 0
    cntlst = [0]*(int(log2(maxx))+1)
    for num in nums:
        bitlst = list(map(int, list(bin(num)[2:])))
        for i in range(len(bitlst)-1,-1,-1):
            cntlst[i] += bitlst[i]

    for i in cntlst:
        if i>1:
            ans += i-1
    return ans


def solution(m, b):
    answer = []

    i, j = 0,0
    for mm in m:
        i=j
        j+=mm
        answer.append(sol(b[i:j]))

    return answer

m = [2,2]
b = [3,2,1,2]
print(solution(m,b))


"""
"""