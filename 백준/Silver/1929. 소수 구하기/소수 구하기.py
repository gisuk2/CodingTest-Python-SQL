import sys
input = sys.stdin.readline

# 1. 입력 받기
M, N = map(int, input().split())

def solve():
    # 2. 체 만들기 (N까지의 모든 수)
    # 처음엔 모두 소수(True)로 초기화
    is_prime = [True] * (N + 1)
    is_prime[0] = is_prime[1] = False
    
    # 3. 에라토스테네스의 체 로직 (제곱근까지만 반복)
    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            # 슬라이싱을 이용한 일괄 수정 (매우 빠름)
            is_prime[i*i : N+1 : i] = [False] * len(range(i*i, N+1, i))
    
    # 4. 출력 (M 이상인 것만)
    # 리스트를 새로 만들지 않고 바로 출력하여 메모리 아낌
    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)

solve()