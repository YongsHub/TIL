def solution(s):
    answer = True
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
    p_count = s.count('p')
    y_count = s.count('y')
    if p_count == 0 and y_count == 0:
        return True
    elif p_count == y_count:
        return True
    else:
        return False
