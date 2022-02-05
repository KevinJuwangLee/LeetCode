import numpy
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        x=[]
        for i in range(len(arr)):
            x.append(sum([abs(l-i) for l in numpy.where(numpy.array(arr) == arr[i])[0]]))
        return x