def addSpaces(s, spaces):
    n = s[:spaces[0]]
    for i in range(len(spaces)-1):
        n+=" " + s[spaces[i]:spaces[i+1]]
    n+=" " + s[spaces[-1]:]
    return n
print(addSpaces("spacing", [0,1,2,3,4,5,6]))