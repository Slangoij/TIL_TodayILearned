import math
str = input()
strs = [str[10*i:10*(i+1)] for i in range(math.ceil(len(str)/10))]
for strr in strs:
    print(strr)