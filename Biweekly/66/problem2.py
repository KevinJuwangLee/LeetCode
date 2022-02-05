
class Solution(object):
    def minimumBuckets(self, street):
        """
        :type street: str
        :rtype: int
        """
        count = 0
        i = 0
        gathered = []
        if street.count("H") == 0:
            return 0
        if street.count(".") == 0:
            return -1
        while i < len(street):
            if i < len(street) - 1 and street[i] == 'H' and street[i + 2] == 'H':
                gathered.append(i)
                gathered.append(i+2)
        i = 0
        while i < len(street):
            if street[i] == '.':
                if i > 0 and street[i - 1] == 'H' and i-1 not in gathered:
                    count = count + 1
                    gathered.append(i - 1)
                if i < len(street) - 1 and street[i + 1] == 'H' and i+1 not in gathered:
                    count = count + 1
                    i = i + 2
                    gathered.append(i + 1)
                    continue
            i = i + 1
        return count

