from collections import Counter

tri = []
for _ in range(3):
    tri.append(int(input()))
summ = 0
for i in tri:
    summ += i

if summ!=180:
    print('Error')
else:
    cnts = Counter(tri).most_common()
    leng = len(cnts)
    if leng==1:
        print('Equilateral')
    elif leng==2:
        print('Isosceles')
    else:
        print('Scalene')