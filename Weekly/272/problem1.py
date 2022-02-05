def firstPalindrome(words):
    for i in words:
        possible = True
        for j in range(len(i)):
            if i[j] != i[len(i)-j-1]:
                possible = False
                break
        if possible:
            return i
    return ""

print(firstPalindrome(["abc","car","ada","racecar","cool"]))