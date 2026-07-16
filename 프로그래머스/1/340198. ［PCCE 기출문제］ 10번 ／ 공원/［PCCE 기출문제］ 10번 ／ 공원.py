# # 오른쪽 1칸이 비어있으면 2x2 체크, 2칸이면 3x3 체크
# # 최대 정사각형 한 변의 길이 2, 3, 5 역순으로 한번씩 루프도는데, 만족하면 바로 다음 체크
# # 모든 칸마다 체크
# def solution(mats, park):
#     answer = 0
#     mats = sorted(mats, reverse=True) 
    
#     # len(park[0]) - 최소길이+1 만큼 반복 / len(park) - 최소길이 + 1만큼 반복
#     for i in mats:
#         for r in range(len(park)-i+1):
#             for c in range(len(park[0])-i+1):
#                 if check(r,c):
#                     retrun size 
#     return True

# def check(a, b):
#     for i in range(a):
#         for j in range(b):
#             if park[a][b] != "-1":
#                 return False
#     return True

# # ###############################################3

def solution(mats, park):
    mats = sorted(mats, reverse=True) 
    
    # 세로, 가로 길이를 미리 구해두면 편합니다.
    H = len(park)
    W = len(park[0])
    
    # 돗자리 크기(size) 하나씩 꺼내기
    for size in mats:
        # 사용자님의 훌륭한 아이디어: 경계선까지만 루프 돌기!
        for r in range(H - size + 1):
            for c in range(W - size + 1):
                # check 함수에 시작 좌표(r, c), 돗자리 크기(size), park를 전달합니다.
                if check(r, c, size, park):
                    return size # 찾으면 즉시 이 돗자리 크기를 반환!
                    
    return -1 # 끝까지 못 찾으면 -1 반환

def check(start_r, start_c, size, park):
    # 시작 좌표부터 돗자리 크기만큼만 딱 검사합니다.
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            # 한 칸이라도 빈 칸("-1")이 아니면 (사람이 있으면) 깔 수 없음
            if park[r][c] != "-1":
                return False
    return True
    