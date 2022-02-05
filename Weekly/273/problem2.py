class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        x=[]
        for i in range(len(s)):
            r=0
            if s[i] == 'D' and startPos[0]+1 < n:
              r=1
            if s[i] == 'U' and 0<=startPos[0]-1:
              r=1
            if s[i] == 'R' and startPos[1]+1 < n:
              r=1
            if s[i] == 'L' and 0<=startPos[1]-1:
              r=1
            for j in range(len(s)-i):
                m=s[i:i+j+1]
                h = m.count('D')-m.count('U')+startPos[0]
                v = m.count('R')-m.count('L')+startPos[1]
                if 0 <= h and h < n and 0<=v and v<n:
                    #print((h, v))
                    #print(m[i:i+j+1])
                    r=j+1
                else:
                  break
            x.append(r)
        return x