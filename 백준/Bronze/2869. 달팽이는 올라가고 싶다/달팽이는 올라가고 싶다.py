# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.



# 시간초과가 나왔네?
# A가 추가되었을때 현재 위치를 체크해야하지않나?
# 다른 수식이 존재하려나
import math

A, B, V = map(int, input().split())

# current_h=0
# cnt=1
# while(True):
#     current_h +=A
#     if current_h >= V:
#         print(cnt)
#         break
#     current_h -=B
#     cnt += 1

print(math.ceil((V-A)/(A-B))+1)

