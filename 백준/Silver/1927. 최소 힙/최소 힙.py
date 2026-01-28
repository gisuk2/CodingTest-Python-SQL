import sys
import heapq
input = sys.stdin.read



data = list(map(int,(input().split())))
n = data[0]
heap=[]

# 배열에 넣고 ~ 가장 작은 값을 찾아서 없애야하네
# 시간제한인데 힙을 쓰란거같은데
for i in data[1:]:

    if i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)
            


