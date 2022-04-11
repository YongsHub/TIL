class Trie:
    dictionary = {}

    def insert(self, word):
        current = self.dictionary
        for i in word:
            if i not in current:
                current[i] = {}
            current = current[i]
        current['*'] = True

    def search(self, word):
        current = self.dictionary
        count = 0

        for i in word:
            if len(current[i]) == 1:
                count += 1
            else:
                count = 0
            current = current[i]
        return len(word) if count == 0 else len(word) - count + 1


def solution(words):
    Tree = Trie()
    answer = 0

    for word in words:
        Tree.insert(word)

    for word in words:
        answer += Tree.search(word)
    return answer
