# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 소수출력 알고리즘.
# 소수란. 1보다 큰 자연수 중 1과 자기 자신으로만을 약수로 가지는 수

# 이런거 첫째줄 입력값은 무시하고 2번째 줄 입력값들을 리스트로 받아와서 계산해도 되는건가
# 아무튼 둘째줄 값들 하나씩 계산해서 개수 세야하니깐...

# 약수를 찾는 계산식은 2부터 자기숫자까지 모두 나눠보는 것밖에 없는데 
# 이때 재귀함수 쓰면되나 근데 어캐쓰지 일단 생각나는대로 써볼까

# num_numbers = int(input())

# num_list = map(int, input().split())

# def sosu(n):
#     for i in range(2,n):
#         if n % i == 0 :
#             return True
        
# count = 0
# for i in num_list :
#     if i > 1 and sosu(i) == True:
#         count += 1

# print(count)

# 1. 코드의 문제점 분석 (Logic Check)
# 나머지 연산자 (%) 미사용: n // i != 0은 몫을 구하는 연산입니다. 소수는 나머지가 0인 숫자가 1과 자기 자신뿐인 수이므로, 반드시 % 연산자를 써야 합니다.

# 판별 로직의 오류: 현재 로직은 한 번이라도 나누어떨어지지 않으면 바로 True를 리턴합니다. 소수가 되려면 2부터 n-1까지 그 어떤 수로도 나누어떨어지면 안 됩니다. 즉, 중간에 하나라도 나누어떨어지면(나머지가 0이면) 그 즉시 False를 줘야 합니다.

# 범위 설정: range(2, n-1)보다는 range(2, n)이 더 명확합니다.

num_numbers = int(input())

num_list = map(int, input().split())

def sosu(n):
    if n < 2:
        return False
    
    for i in range(2,n):
        # // 몫 계산, % 나머지 연산
        if n % i == 0: # n을 i로 나누었을 때 나머지가 0이다? 나눠졌네? 소수가 아니다
            return False
        
    return True
        
count = 0
for i in num_list :
    if sosu(i) == True:
        count += 1

print(count)