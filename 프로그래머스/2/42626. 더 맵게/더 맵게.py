import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    
    while len(scoville) > 0:
        min = heapq.heappop(scoville)
        if min >= K:
            return count
        elif len(scoville)==0:
            return -1
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville,min+min2*2)
            count += 1