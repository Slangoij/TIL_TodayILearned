from collections import deque

def solution(n, edge):
    mapp = [[] for _ in range(n+1)]
    for stt,end in edge:
        mapp[stt].append(end)
        mapp[end].append(stt)

    vstd = [False]*(n+1)
    q = deque([[1,0]])
    vstd[1] = True
    answer = 0
    maxdist = 0
    while q:
        nownode, dist = q.popleft()
        for nxtnode in mapp[nownode]:
            if not vstd[nxtnode]:
                vstd[nxtnode] = True
                q.append([nxtnode, dist+1])
                if dist+1>maxdist:
                    answer = 1
                    maxdist = dist+1
                else:
                    answer += 1
    
    return answer

n = 6
edge = [[1,2],[1,3],[1,5],[2,5],[5,6],[6,2],[2,4]]

print(solution(n,edge))
"""

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

n = 4
edge = [[1,2],[2,4],[1,3]]

"""