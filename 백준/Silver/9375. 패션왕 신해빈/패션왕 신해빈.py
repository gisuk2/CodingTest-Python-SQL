import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    dic = {}
    
    # 1. 카테고리(b)별로 의상의 개수 세기
    for _ in range(n):
        a, b = input().split()
        if b in dic: # .keys()는 생략해도 dict에서 바로 키를 찾습니다.
            dic[b] += 1
        else:
            dic[b] = 1
            
    # 2. 경우의 수 계산하기
    ans = 1
    for count in dic.values():
        # (해당 종류의 의상 수 + 안 입는 경우 1개)를 곱함
        ans *= (count + 1)
        
    # 3. 아무것도 안 입은 경우(1)를 빼고 출력
    print(ans - 1)