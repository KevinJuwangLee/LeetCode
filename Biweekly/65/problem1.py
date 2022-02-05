def checkAlmostEquivalent(self, word1, word2):
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for i in letters:
        if word1.count(i) - word2.count(i) > 3 or word2.count(i) - word1.count(i) > 3:
            return False
    return True