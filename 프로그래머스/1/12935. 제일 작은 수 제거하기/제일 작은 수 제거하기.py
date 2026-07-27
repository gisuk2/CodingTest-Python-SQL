# def solution(arr):
#     answer = []
#     min = 0
#     arr1 = arr.sort(reverse = True)
#     min = arr1[:-1]
#     for i in range (len(arr)):
#         if arr[i] == min:
#             arr.pop(i)
#             break
#     if len(arr) != 0:
#         answer = arr
#     else:
#         answer = [-1]
#     return answer

def solution(arr):
    # 1. 가장 작은 값을 찾아서 리스트에서 제거합니다.
    arr.remove(min(arr))
    
    # 2. 제거 후 리스트가 비어있다면 [-1]을, 아니라면 남아있는 arr을 반환합니다.
    return arr if len(arr) > 0 else [-1]