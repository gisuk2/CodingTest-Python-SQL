#  X 다 지우고 리스트로 저장한다음 시그마로 계산해야하나

T = int(input())
total=0
cnt = 0
for i in range(T):
    total=0
    cnt = 0
    val = list(input())
    for j in range(len(val)):
        if val[j]=='O':
            if j>0:
                if val[j-1]=='O':
                    cnt += 1
            total += cnt+1
        else:
            cnt = 0
    print(total)

# 조건문 줄이고 다른방식 도입
# X 를 기준으로 나누는게 필요해보이는데 seperate 가 파이썬에 있나?
# split() 으로는 무리일 것 같은데
# 돌겠네 separate 배운 적이 없는데 아닌 것 같기도 하고




    
    

