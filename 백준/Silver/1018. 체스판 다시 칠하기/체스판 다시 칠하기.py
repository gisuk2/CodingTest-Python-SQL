import sys
input = sys.stdin.readline

N, M = map(int, input().split())

patt = [input().strip() for _ in range(N)]
result_li = []
# 입력 받을건 다 받았고, 이제 돋보기로 체크 반복문


for i in range(N-7):
    for j in range(M-7):

        draw_W = 0
        draw_B = 0
        # 이게 완벽한 체스판인지 판별하는 반복문, 아니면 카운트+
        for a in range(i, i+8):
            for b in range(j, j+8):
                # 짝수 자리일때 W가 아니면 색칠
                if (a+b)%2==0 :
                    if patt[a][b] != 'W':
                        draw_W += 1
                    if patt[a][b] != 'B':
                        draw_B += 1
                else :
                    if patt[a][b] != 'B':
                        draw_W += 1
                    if patt[a][b] != 'W':
                        draw_B += 1

# 이제 받아야하는게 반복문 끝나면 그린것들을 리스트에 넣어야함
        result_li.append(draw_B)
        result_li.append(draw_W)

print(min(result_li))


