class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word='a'+word+'a'
        s={int("".join(y)) for x,y in groupby(word, key=str.isalpha) if not x}
        return len(s)        