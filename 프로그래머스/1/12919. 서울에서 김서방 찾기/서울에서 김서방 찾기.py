def solution(seoul):
    c = 0
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            c = i
            break  # 찾았으면 루프 종료!
            
    # c를 다 구한 뒤에 f-string으로 결과 문자열 생성
    answer = f'김서방은 {c}에 있다'
    return answer