N = int(input())
dic = {chr(ord('A')+i):0 for i in range(26)}
for _ in range(N):
    word = list(input().strip())
    leng = len(word)
    for i in range(leng):
        dic[word[i]] += 10**(leng-i-1)

cnts = sorted(list(dic.items()), key=lambda x: -x[1])
num, answer = 9, 0
for i,cnt in cnts:
    if not cnt:
        break
    answer += num * cnt
    num -= 1

print(answer)