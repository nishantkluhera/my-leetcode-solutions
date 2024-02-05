class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        has_cache = [False] * (N + 1)
        cache = [None] * (N + 1)

        def findOptimalSum(index):
            if index >= N:
                return 0
            if has_cache[index]:
                return cache[index]

            currentMax = 0
            maxPartitionSum = 0

            for i in range(min(k, N - index)):
                currentMax = max(currentMax, arr[index + i])
                maxPartitionSum = max(maxPartitionSum, findOptimalSum(index + i + 1) + (i + 1) * currentMax)

            has_cache[index] = True
            cache[index] = maxPartitionSum
            return maxPartitionSum

        return findOptimalSum(0)                                      