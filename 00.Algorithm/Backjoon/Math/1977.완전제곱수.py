m = int(input())
n = int(input())

rm, rn = m**(1/2), int(n**(1/2))
if rm - int(rm) > 0:
    rm = int(rm)+1
else:
    rm = int(rm)
if rm>rn:
    print(-1)
else:
    answer = 0
    for i in range(rm,rn+1):
        answer += i**2
    print(answer)
    print(rm**2)