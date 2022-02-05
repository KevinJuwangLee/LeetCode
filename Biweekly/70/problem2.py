class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mini=0
        maxi=-float(inf)
        s=0
        for i in differences:
            s+=i
            mini=min(s,mini)
            maxi=max(s,maxi)
        print((mini, maxi))
        l=lower
        u=upper
        l-=mini
        u-=maxi
        print((l,u))
        if l <= u:
            return min(upper, u)-max(lower, l)+1
        return 0
            
