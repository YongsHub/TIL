def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    answer = ''

    for alpha in s:
        if alpha.isupper():
            alpha = alpha.lower()
            idx = alphabet.index(alpha)
            answer += alphabet[idx + n].upper()
        elif alpha.islower():
            idx = alphabet.index(alpha)
            answer += alphabet[idx + n]
        else:
            answer += ' '
    return answer
