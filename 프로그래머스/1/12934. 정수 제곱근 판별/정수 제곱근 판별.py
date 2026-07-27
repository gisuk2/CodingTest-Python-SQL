def solution(n):
    x = n ** 0.5
    # x가 1로 나누어 떨어지면(정수이면) (x+1)^2 리턴, 아니면 -1 리턴
    return int(x + 1) ** 2 if x % 1 == 0 else -1