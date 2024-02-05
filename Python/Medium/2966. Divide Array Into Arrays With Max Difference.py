class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()

        ans = []

        for i in range(0, N, 3):
            batch = nums[i:i + 3]
            if len(batch) == 3 and batch[2] - batch[0] <= k:
                ans.append(batch)

        return ans if len(ans) * 3 == N else []            