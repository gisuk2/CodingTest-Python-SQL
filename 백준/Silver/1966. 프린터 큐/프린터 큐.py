import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())


for _ in range(T):
    N, M = map(int, input().split())
    priorities = list(map(int, input().split()))
    queue = deque([(p, i) for i,p in enumerate(priorities)])
    
    cnt = 0
    # 정렬후 첫 정수와 중요도를 비교해서 삭제/넘기기 cnt+1
    # 찾는거와 같다면 종료 후 cnt+1, 결과출력
    # 큰수부터 다 쳐내고, 그다음 수 쳐내고.. 나일때 같으면 출력
    priorities.sort(reverse=True)
    # priorities = (sorted(priorities, reverse=True))

    while queue:
        current = queue.popleft()

        if current[0] == priorities[cnt]:
            cnt += 1

            if current[1] == M:
                print(cnt)
                break
        else:
            queue.append(current)

        
