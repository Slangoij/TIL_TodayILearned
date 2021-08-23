from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for cor in course:
        candidates = []
        for order in orders:
            for tmpmenu in combinations(order, cor):
                candidates.append("".join(sorted(tmpmenu)))
        srtd_candidates = Counter(candidates).most_common()
        answer += [menu for menu, cnt in srtd_candidates\
             if cnt>1 and cnt==srtd_candidates[0][1]]
    
    return sorted(answer)

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]	
print(solution(orders,course))

# # 1번째 시도: 모든 조합에 대해 각각의 조합에 대한 전체 메뉴를 일일이 찾아봐야 한다. 
# for cor in course:
#     menuhubo = []
#     if len(menu) >= cor:
#         maxcnt = 0
#         for combi in combinations(menu,cor):
#             cstmer_cnt = 0
#             for order in orders:
#                 chk = True
#                 for lttr in combi:
#                     if lttr not in order:
#                         chk = False
#                         break
#                 if chk:
#                     cstmer_cnt +=1
#             if cstmer_cnt >= 2:
#                 if cstmer_cnt > maxcnt:
#                     menuhubo = ["".join(sorted(combi))]
#                     maxcnt = cstmer_cnt
#                 elif cstmer_cnt == maxcnt:
#                     menuhubo.append("".join(sorted(combi)))

#         answer.extend(menuhubo)
#         menuhubo.clear()