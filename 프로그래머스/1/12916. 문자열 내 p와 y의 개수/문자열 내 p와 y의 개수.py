def solution(s):
    s = s.lower()
    p_c = 0
    y_c = 0
    for i in s:
        if i == 'p': p_c += 1
        if i == 'y': y_c += 1
    return True if p_c == y_c else False