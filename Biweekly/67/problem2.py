class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        robDays = []
        for i in range(time, len(security) - time):
            if security[i - time: i+1] == (sorted(security[i - time: i+1]))[::-1] and security[i: i + time+1] == sorted(security[i: i + time+1]):
              robDays.append(i)
        return robDays
    