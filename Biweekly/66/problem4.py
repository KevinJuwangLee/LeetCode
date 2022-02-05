class Solution(object):
    def countPyramids(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        ones = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones.append([j, i])
        for [x, y] in ones:
            if [x-1, y] in ones and [x+1, y] in ones and [x, y+1] in ones:
                count = count + 1
                
        print(count)