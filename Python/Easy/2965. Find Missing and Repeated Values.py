class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        N=len(grid)
        seen_nums=set()
        repeated,missing=0,0
        for row in range(N):
            for col in range(N):
                num=grid[row][col]

                if num in seen_nums:
                    repeated=num
                else:
                    seen_nums.add(num)

        for i in range(1,N**2+1):
            if i not in seen_nums:
                missing=i
                break

        return [repeated,missing]    

 #complexity: O(N^2) 