class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        x=[i.count('1') for i in bank if i.count("1")!=0]
        if len(x)==0 or len(x)==1:
            return 0
        s=[]
        for i in range(len(x)-1):
            s.append(x[i]*x[i+1])
        return sum(s)