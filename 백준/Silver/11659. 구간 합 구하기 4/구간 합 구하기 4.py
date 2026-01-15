# 시간초과가 떴다...
# 어디서 시간을 많이쓰나 보자..
# for문인거 같은데... a,b 저장하는건 흠 아닌거같고 
# li 생성? 슬라이싱 출력? sum?

# 1. 출력을 join으로 한번에 넣어보자 (ans리스트에 저장 시 문자열로 변환)
# 쇼발 아니네

# 두개씩 합한 값을 저장해두면, 범위 나왔을때 바로 넣을 수 있나
# 2. a, b 저장을 for문 밖으로 꺼내자
# 아오 쇼바 이것도 아니네

# 진짜 dp마냥 더해야하나ㅏㅏㅏㅏ근데 수가 많아지면 에바아닌가?
# 왜 시간초과지

# 아예 read로 다 읽고... 슬라이싱?
# 근데 그게 시간단축이 엄청 크진 않을거같은데

# sum()함수나 슬라이싱이 시간이 엄청걸리나

# 3. 아예 전체 read로 읽어버리자
#######################################################
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# li = list(map(int, input().split()))
# ans = []
# ran = list(map(int, sys.stdin.read().split()))
# # print(ran)
# for i in range(M):
#     a, b = ran[i*2] , ran[1+i*2]
#     # print(a,b)
#     ans.append(str(sum(li[a-1:b])))

# # print(ans)
    
# print('\n'.join(ans))
#######################################################
import sys
input = sys.stdin.read
data = list(map(int, input().split()))
# print(data)

N, M = data[0], data[1]

li = data[2:2+N]
queries = data[2+N:]

prefix_sum = [0]*(N+1)
temp_sum = 0

for i in range(N):
    temp_sum += li[i]
    prefix_sum[i+1] = temp_sum

ans = []
for i in range(M):
    a = queries[i*2]
    b = queries[1+ i*2]
    result = prefix_sum[b] - prefix_sum[a-1]
    ans.append(str(result))

sys.stdout.write('\n'.join(ans) + '\n')
#######################################################
# 무조건 for문 안쪽이 문제다


