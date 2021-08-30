import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    func = input().strip()
    n = int(input())
    tmpnums = input()
    if n>0:
        nums = list(map(int,tmpnums[1:-2].split(',')))
    else:
        nums = []

    if func.count('D') > n:
        print('error')
    else:
        revers = False
        fnt,bck = 0,0
        for work in func:
            if work == 'R':
                revers = not revers
            elif work == 'D':
                if revers:
                    bck += 1
                else:
                    fnt += 1

        ans = nums[fnt:]
        if revers:
            ans.reverse()
            ans = ans[bck:]
        elif bck:
            ans = ans[:-bck]
        print('['+",".join(map(str,ans))+']')

"""

4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]

1
RDRDD
5
[1,2,3,4,5]
[4,5]

"""