# # 빈칸은 ".", 파일이 있는 칸은 "#"의 값을 가집니다.
# # (세로 좌표, 가로 좌표)로 표현
# # [lux, luy, rdx, rdy]


# # 2차원 리스트 값들 중 가장 가장 왼쪽/위쪽 #값 위치를 찾아내 lux, luy에 넣고
# # 가장 오른쪽/아래 #값 위치를 찾아내 rdx, rdy에 넣으면 될 듯함
# # 입력되는 wallpaper 리스트를 2차원리스트로 변환
# # 가장 왼쪽값, 위, 아래, 오른쪽 각각 4번을 탐색해야 할 듯
# # 아래서부터 위 탐색?
# # 문자열#이 있는 위치를 모두 좌표로 나타내면 찾을 수 있나?



# def solution(a):
#     lux= luy= rdx= rdy = 0
#     wallpaper_l = list(map(str, wallpaper.split(,)))
#     n_list = []
    
#     for i in range(len(wallpaper_l)):
#         for j in range(len(wallpaper_l[i])):
#             if wallpaper_l[i][j] == '#':
#                 n_list.appand([i,j])
                
                
# #   찾으려는게 i의 최대 최소, j의 최대 최소값 4개를 모두 구하려고한다
#     ruy = max(n_list)[0]
#     rux = max(n_list)[1]
#     lux = min(n_list)[0]
#     luy = max(n_list)[1]
#     # min_val = min(map(min, n_list))
#     # max_val = min(map(min, n_list))
#     answer = [lux, luy, rdx, rdy]
#     return answer


def solution(wallpaper):
    # 1. '#'이 있는 모든 행(i)과 열(j)의 인덱스를 저장할 리스트
    rows = []
    cols = []
    
    # 2. 2차원 배열(리스트) 탐색
    for i in range(len(wallpaper)):      # 세로(행)
        for j in range(len(wallpaper[i])): # 가로(열)
            if wallpaper[i][j] == '#':
                rows.append(i)
                cols.append(j)
    
    # 3. 각 좌표의 최소값과 최대값 찾기
    # 시작점(lux, luy)은 가장 작은 값
    # 끝점(rdx, rdy)은 가장 큰 값에 1을 더해야 함 (칸이 아니라 점 기준이라서)
    lux = min(rows)
    luy = min(cols)
    rdx = max(rows) + 1
    rdy = max(cols) + 1
    
    return [lux, luy, rdx, rdy]