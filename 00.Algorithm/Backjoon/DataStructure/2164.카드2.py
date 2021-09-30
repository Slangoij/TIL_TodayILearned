from collections import deque
n = int(input())
cards = deque(i for i in range(1,n+1))
while cards:
    ans = cards.popleft()
    if cards:
        ans = cards.popleft()
        cards.append(ans)
    else:
        break
print(ans)