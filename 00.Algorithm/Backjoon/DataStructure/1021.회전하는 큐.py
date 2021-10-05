n, m = map(int,input().split())
lst = [i for i in range(1,n+1)]
todos = list(map(int, input().split()))
ans = 0
for todo in todos:
    i = lst.index(todo)
    lst = lst[i+1:] + lst[:i]
    ans += min(i, n-i)
    n -= 1
print(ans)

# # 1번째 시도: 일일이 리스트를 앞에서부터 조회했다. list의 index깜빡
# n, m = map(int,input().split())
# lst = [i for i in range(1,n+1)]
# todos = list(map(int, input().split()))
# ans = 0
# for target in targets:
#     for i in range(n):
#         if lst[i] == target:
#             lst = lst[i+1:] + lst[:i]
#             if i <= (n-1)//2:
#                 ans += i
#             else:
#                 ans += n-i
#             break
#     n -= 1
# print(ans)