def solution(n):
    answer = []
    
    def hanoi(n, start, end, mid):
        # 원반이 1개일 때가 재귀의 기저 조건(Base Case)
        if n == 1:
            answer.append([start, end])
            return
        
        # 1. n-1개를 시작점에서 경유지로 옮긴다 (목적지를 경유지로 활용)
        hanoi(n - 1, start, mid, end)
        
        # 2. 가장 큰 원반을 시작점에서 목적지로 옮긴다
        answer.append([start, end])
        
        # 3. 경유지에 있던 n-1개를 목적지로 옮긴다 (시작점을 경유지로 활용)
        hanoi(n - 1, mid, end, start)

    # 1번 기둥에서 3번 기둥으로 n개를 옮기며, 2번을 경유지로 사용
    hanoi(n, 1, 3, 2)
    return answer