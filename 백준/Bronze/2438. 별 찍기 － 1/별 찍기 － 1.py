# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

# 반복문을 사용하면 될 듯함
# 1번에는 1개 2번에는 2개... 이어서

s_cnt = int(input())
answer = ''
for i in range(s_cnt) :
    answer += '*'
    print(answer)