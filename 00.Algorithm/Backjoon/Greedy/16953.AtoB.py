a,b = map(int, input().split())
ans = 1
while b>a:
    if b%2 == 0:
        b /= 2
    elif b%10 != 1:
        ans = -1
        break
    elif b-1 >= 10:
        b = (b-1)/10
    ans += 1

if b < a:
    ans = -1

print(ans)