class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s:
            return True
        if 'b' not in s:
            return True
        return len(s) - (s[::-1].index('a')) - 1 < s.index('b')