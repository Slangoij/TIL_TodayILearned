import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 첫번째 풀이, DFS를 이용한 위상정렬 풀이에 추가적으로 
# 방문할 첫번째 노드들을 정리한 primes리스트를 정리하여
# 풀이했더니 70프로 정도에서 틀림.

# 원인은 키를 재지 않았던 인원!!

mapp = [[] for key in range(N+1)]
primes = [False]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    mapp[A].append(B)
    primes[A], primes[B] = True, False

vstd = [False] *(N+1)
answer = []
def dfs(x):
    vstd[x] = True
    if mapp[x]:
        for nxt_node in mapp[x]:
            if not vstd[nxt_node]:
                dfs(nxt_node)
    answer.append(x)
        

for i in range(1,N+1):
    if primes[i] and not vstd[i]:
        dfs(i)
for i in range(1,N+1):
    if not vstd[i]:
        answer.append(i)

answer.reverse()
print(" ".join(map(str,answer)))

"""

3 2
1 3
2 3

4 2
4 2
3 1

3 3
1 3
2 3
1 2

8 8
1 2
2 3
3 7
3 8
2 6
1 4
4 5
6 3

5 3
1 3
1 2
2 3
"""