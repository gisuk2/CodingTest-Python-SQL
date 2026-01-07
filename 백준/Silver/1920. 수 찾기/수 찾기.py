# # 시간초과 문제
# # 입력방식 변환 -> sys 한번에 X
# # 형변환 한번에 X
# # 리스트 저장방식 -> 컴프리헨션 X
# # 출력방식 -> 저장 후 print 한번 X
# # join 써봐야할듯 X

# # 아니면 첫줄만 저장하고 나머지는 입력될때마다 바로 결과값계산?
# # append 가 시간이 많이걸리는 작업인가?
# # 일단 정수의 크기가 엄청나게 큼 -> 저장 부분에서 뭔가 처리해야하나?
# # 아니 입력된 값을 공백으로 나누고 그 값을 처음부터 처리하려면 저장해야하는건 필수아닌가?

# # True False가 문제인가?
# # in() 함수 시간이 오래걸리나? find? 존재여부 확이만하는데 in 맞는데 index 필요없잖아

# # 검색방법? 버블? 힙? 순차? 이진트리?
# # True 면 1 False 0 으로 미리 저장하고 case 쓰는게 더 빨라? 형변환보다?




# import sys
# input = sys.stdin.readline

# li=[]
# for _ in range(2):
#     N = int(input())
#     li.append([_ for _ in input().split()])

# answer =[]
# for i in range(N):
#     answer.append(int(li[1][i] in li[0]))

# print("\n".join(map(str, answer)))


import sys
input = sys.stdin.readline

_ = input() # N은 굳이 안 써도 되니 버림
own = set(input().split()) # 탐색용은 set으로!
_ = input() # M도 버림
check = input().split()

# 리스트 컴프리헨션 + join으로 한방에 출력
print("\n".join("1" if x in own else "0" for x in check))