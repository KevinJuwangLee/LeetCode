class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        n=0
        x=[i for i in words if i[::-1] in words]
        for i in x:
            if i[0]!=i[1]:
                n+=min(x.count(i), x.count(i[::-1]))*4
                x=[s for s in x if s!=i and s!=i[::-1]]
                continue
            c=x.count(i)
            if i[0]==i[1] and c>=2:
                if c%2==0:
                    n+=c*2
                    x=[s for s in x if s!=i]
                    continue
                n+=c*2-2
                x=[s for s in x if s!=i]+[i]
        for i in x:
            if i[0]==i[1]:
                n+=2
                break
        return n