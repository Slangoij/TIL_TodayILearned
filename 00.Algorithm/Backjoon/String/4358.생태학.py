import sys
input = sys.stdin.readline

strr = input().strip()
dictt = {}
whole_cnt = 0
while strr:
    if strr not in dictt:
        dictt[strr] = 0
    dictt[strr] += 1
    whole_cnt += 1
    strr = input().strip()

for name, cnt in sorted(list(dictt.items()), key=lambda x: x[0]):
    # print(name, round(cnt*100/whole_cnt, 4))
    print("%s %.4f" % (name, cnt / whole_cnt * 100))
