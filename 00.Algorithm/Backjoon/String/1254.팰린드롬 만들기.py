strs = list(input().strip())
leng = len(strs)
mid = (leng+1)//2-1
sub = strs[:mid]
for i in range(mid,leng):
    sub += strs[i]
    if list(reversed(sub[:-1]))[:leng-i-1] == strs[i+1:]:
        print(i*2+1)
        break
    elif list(reversed(sub))[:leng-i-1] == strs[i+1:]:
        print((i+1)*2)
        break
