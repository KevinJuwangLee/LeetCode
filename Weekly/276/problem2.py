class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        while target > 1:
            if maxDoubles>0 and target%2==0:
                target=target//2
                maxDoubles-=1
                c+=1
                continue
            if maxDoubles>0 and target%2==1:
                target-=1
                c+=1
                continue
            if maxDoubles==0:
                c+=target-1
                target=1
        return int(c)