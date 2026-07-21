def solution(n):
    answer = 0
    li = [x for x in str(n)]
    li.sort(reverse = True)
    answer = int("".join(li))
    return answer