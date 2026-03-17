# def solution(x):
#     sum=0
#     temp = x
#     while x//10 > 10:
#         sum += x%10
#         x = x//10
#     return True if temp % sum == 0 else False


def solution(x):
    total_sum = 0
    temp = x
    
    while x > 0:
        total_sum += x % 10  # 마지막 자릿수 추출
        x //= 10             # 마지막 자릿수 제거
        
    return temp % total_sum == 0