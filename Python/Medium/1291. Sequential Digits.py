class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        mapper = "123456789"
        output = []

        low_len, high_len = len(str(low)), len(str(high))

        for d in range(low_len, high_len + 1):
            for i in range(0, 10 - d):
                cand = int(mapper[i:i + d])
                if cand < low:
                    continue
                if cand > high:
                    break
                output.append(cand)

        return output