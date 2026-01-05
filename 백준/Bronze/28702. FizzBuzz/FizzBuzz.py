# 문제
# FizzBuzz 문제는 
# $i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

#  
# $i$가 
# $3$의 배수이면서 
# $5$의 배수이면 “FizzBuzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수이지만 
# $5$의 배수가 아니면 “Fizz”를 출력합니다.
#  
# $i$가 
# $3$의 배수가 아니지만 
# $5$의 배수이면 “Buzz”를 출력합니다.
#  
# $i$가 
# $3$의 배수도 아니고 
# $5$의 배수도 아닌 경우 
# $i$를 그대로 출력합니다.
# FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?



# 함수 만들기같은데 입력된 문자열or숫자 보고 다음 출력될 문자값 계산
# 그걸 함수에 넣어서 출력
# match-case 써볼까
# 입력값을 저장해둬야 그다음 올 문자열을 알겠다

# 어 Fizz Buzz 숫자 보고 규칙을 알아야하네?
# 3문자열 중에 숫자로된거 찾고 그걸로 출력값 찾아야하나?
# 무조건 1~2개는 숫자 아닌가??

import sys
input = sys.stdin.readline

def FizzBuzz(data):
    match data:
        case n if n%3 ==0 and n%5==0:
            print('FizzBuzz')
        case n if n%3 ==0 and n%5!=0:
            print('Fizz')
        case n if n%3 !=0 and n%5==0:
            print('Buzz')
        case _:
            print(data)

# 3번 나오는 문자열중에 숫자있으면 그 index 에 따라 +@
# 입력값이 intger 인지 str인지 알아야할 듯 한데
# 그러면 isInt? 이런게 있나?
# answer 부분에서 int 형식으로만
# type()으로 확인하면 되겠다
# 입력값을 type() 으로 봐서 int형이면 조건문을 타는게 맞지않나?

for i in range(1,4):
    ans = (input().strip())
    if ans.isdigit():
        ans = int(ans)
        if i==1 :
            ans += 3
            FizzBuzz(ans)
            break
        elif i==2:
            ans += 2
            FizzBuzz(ans)
            break
        elif i==3:
            ans += 1
            FizzBuzz(ans)
            break


