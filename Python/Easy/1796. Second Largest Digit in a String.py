class Solution:
    def secondHighest(self, s: str) -> int:
        return (list(sorted(set(int(x)for x in s if x.isdigit()),reverse=True))+[-1,-1])[1]