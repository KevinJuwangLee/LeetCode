class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        odds = [i for i in nums if i%2==1]
        evens = [i for i in nums if i%2==0]
        one = odds[:int(len(odds)/2)] + evens[:int(len(evens)/2)]
        two = odds[int(len(odds)/2):] + evens[int(len(evens)/2):]
        return [int((one[i]+two[i])/2) for i in range(len(one))]