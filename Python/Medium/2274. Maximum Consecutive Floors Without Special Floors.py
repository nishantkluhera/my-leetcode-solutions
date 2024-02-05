class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.extend([bottom-1, top+1])
        special.sort()

        return max(y - x - 1 for x, y in zip(special, special[1:]))  

        #used max & a generator expression within because recently learnt what a generator expression is
        #shouldn't this be under easy ???