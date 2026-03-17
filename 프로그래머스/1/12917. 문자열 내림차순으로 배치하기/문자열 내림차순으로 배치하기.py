def solution(s):
    res = sorted(s, reverse=True)

        # 2. 리스트를 다시 하나의 문자열로 합쳐줍니다.
    return "".join(res)