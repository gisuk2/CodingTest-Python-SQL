# 문제 이해하는데 6분걸렸다...
# 첫 줄은 입력 둘째줄의 값들을 T와 각각 비교해서 count+ 하면 될것같고
# 둘째 줄은 입력 첫째줄의 값을 P 로 나눈값의 몫과 나머지를 더하면 나올듯
# 이것도 입력값 한줄씩 받고 3번째에서 마무리해야하는데
# 아 이거 입력어떻게받지 한줄 읽고 다음줄은 다르게 계산해야하는데
# 이걸 다 조건문으로 하기는 어렵지않나 해볼까


# 1. 수정이 필요한 부분
# ① 티셔츠 묶음 수 계산 로직
# 현재 (i % T) + 1 형식을 사용하셨는데, 이는 잘못된 묶음 수를 산출합니다.

# 만약 i가 T의 배수라면? 예를 들어 6명을 3명씩 묶을 때, 6 % 3 + 1 = 1이 되어 1묶음만 나옵니다(실제로는 2묶음 필요).

# 정석 로직: i를 T로 나눈 몫을 취하되, 나머지가 있을 때만 1을 더해줘야 합니다.

# ② 펜 출력 순서 및 변수
# 문제에서 요구하는 출력은 (펜 묶음 수, 남은 낱개 수) 순서입니다.

# num_participants는 input()으로 받았을 때 문자열이므로 계산을 위해 int()로 형변환이 반드시 필요합니다.

count=0

num_participants = int(input())
num_Tsize_list = list(map(int, input().split()))
num_TP_list = list(map(int, input().split()))

for i in num_Tsize_list :
    count += (i // num_TP_list[0])

    if i % num_TP_list[0] != 0:
        count += 1



count_P_total = num_participants//num_TP_list[1]
count_p_solo = num_participants%num_TP_list[1]

print(count)
print(count_P_total, count_p_solo)


    
    

