numlst = list(input().strip())
numlst.sort(reverse=True)
if sum(list(map(int, numlst[:-1]))) % 3 == 0 and numlst[-1] == '0':
    print("".join(numlst))
else:
    print(-1)