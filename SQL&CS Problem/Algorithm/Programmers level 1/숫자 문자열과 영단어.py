def solution(s):
    answer = []
    words = []
    dictionary = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                  'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for alphabet in s:
        if alphabet.isalpha():
            words.append(alphabet)
        else:
            answer.append(alphabet)

        word = ''.join(words)

        if word in dictionary:
            answer.append(dictionary[word])
            words = []

    return int(''.join(answer))
