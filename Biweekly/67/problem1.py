class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        big = []
        biggestIndices = []
        numsCopy = [i for i in nums]
        for i in range(k):
            maxx = -100000
            for s in range(len(nums)):
                if nums[s] > maxx:
                    maxx = nums[s]
                    maxInd = s
                  
        nums.remove(maxx)
        biggestIndices.append(maxInd)
        for i in biggestIndices:
            big.append(numsCopy[i])
        return big