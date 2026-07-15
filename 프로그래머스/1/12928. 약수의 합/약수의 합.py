# 약수 변수 찾기, 더하기
# 1부터 n까지 나눴을때 나머지가 0
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
            
    return answer