class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2!=0:return []
        t=finalSum//2
        r=[]
        s=1
        while t>0:
            if s<=t:
                r.append(s)
                t-=s
                s+=1
            else:
                r[-1]=r[-1]+t
                t=0
        return [2*i for i in r]