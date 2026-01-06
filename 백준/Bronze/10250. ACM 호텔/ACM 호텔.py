#  계수 정렬? 각 방마다 거리를 넣어? 규칙성을 찾아?
# 규칙성있게 하는것도? ㄴㄴ 직사각형이라 원이 아니야
# 방마다 거리 입력? ㄱㅊ을듯? dict은 피료없을듯

# 규칙이 나았나...? ㅈ댔네 정렬을 어캐하지?
# 아니 그냥 순서였네 좌하단이 0이 아니였구나 뭐하냐
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    ho = N // H + 1

    if floor == 0:
        floor = H    # 나머지가 0이면 최고층(H)으로 변경
        ho -= 1      # 호수는 하나 줄여줌

    # 층수에 100을 곱해서 호수와 더함
    print(floor * 100 + ho)

    # hotel = [[0]*W for _ in range(H)]

    # li = []

    # for i in range(H):
    #     for j in range(W):
    #         hotel[i][j] = j+1
    #         li.append(hotel[i][j])

    # # sorted(li)
    # print(li[5])
    # answer = li[N+1]
    # print(answer)
