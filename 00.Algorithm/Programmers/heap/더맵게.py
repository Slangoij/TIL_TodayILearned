import heapq

def solution(scoville, K):
    answer = 0
    
    leng = len(scoville)
    heapq.heapify(scoville)
    chk = False
    for _ in range(leng-1):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a>=K and b>=K:
            chk = True
            break
        heapq.heappush(scoville, min(a,b)+2*(max(a,b)))
        answer += 1
    if not chk and scoville[0] < K:
        answer = -1
    
    return answer