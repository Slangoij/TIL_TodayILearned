n = int(input())
a, b = 1, 2
for i in range(n-2):
    a, b = b%15746, (a+b)%15746
if n > 1:
    print(b%15746)
else:
    print(1)