class Solution:
    def numberOfWays(self, corridor: str) -> int:
        s=[i for i in range(len(corridor)) if corridor[i]=="S"]
        if len(s)%2 or len(s)==0:
            return 0
        t=[s[2*r+2]-s[2*r+1] for r in range(len(s)//2-1)]
        p=1
        for i in t:
            p*=i
        return p%(10**9+7)