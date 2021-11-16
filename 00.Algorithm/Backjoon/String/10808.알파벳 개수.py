# from collections import Counter
s = list(input().strip())
# print(list(Counter(s).values()))
dic = {chr(ord('a')+i): 0 for i in range(26)}
for let in s:
    dic[let] += 1
print(" ".join(map(str, list(dic.values()))))