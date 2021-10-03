dp = [1,1,1,2,2]
todo = []
maxx = 0
for _ in range(int(input())):
    tmp = int(input())
    todo.append(tmp)
    maxx = max(maxx, tmp)
for i in range(5,maxx+1):
    dp.append(dp[i-5]+dp[i-1])
for num in todo:
    print(dp[num-1])