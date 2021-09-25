txt = input().strip()
word = input().strip()

tlen,wlen = len(txt), len(word)
i,ans = 0, 0
while i <= tlen-wlen:
    ni = txt.find(word, i)
    if ni == -1:
        break
    i = ni + wlen
    ans += 1

print(ans)