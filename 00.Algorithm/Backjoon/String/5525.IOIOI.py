n = int(input())
m = int(input())
s = input().strip()
pn = 'I'+'OI'*n
leng = 1+2*n
i,ans = 0,0
while i <= m-leng:
    if s[i:i+leng] == pn:
        ans += 1
        i += leng
        while s[i:i+2] == 'OI':
            ans += 1
            i += 2
    else:
        i += 1
print(ans)
"""
a
"""