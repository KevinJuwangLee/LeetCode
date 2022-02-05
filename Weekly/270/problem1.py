class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        even = []
        evenNumbers = []
        for i in digits:
            if i % 2 == 0 and i not in even:
                even.append(i)
        if len(even) == 0:
            return []
        for i in even:
            for x in digits:
                for y in digits:
                    if ((x == i or y == i) and digits.count(i) == 1) or ((x == i and y == i) and digits.count(i) < 3) or x == 0 or (x == y and digits.count(x) == 1):
                        continue
                    num = 100*x + 10*y + i
              
                    if evenNumbers.count(num) == 0:
                        evenNumbers.append(num)
        return sorted(evenNumbers)
                
        