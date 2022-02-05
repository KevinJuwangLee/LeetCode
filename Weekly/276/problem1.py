class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        if len(s)%k !=0:
            s+=fill*(k-(len(s)%k))
        return [s[k*i:k*(i+1)] for i in range((len(s)//k))]