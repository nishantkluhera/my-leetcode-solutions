class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        std::string result;
        size_t len1 = word1.length();
        size_t len2 = word2.length();
        size_t maxLen = std::max(len1, len2);

        for (size_t i = 0; i < maxLen; ++i) {
            if (i < len1) {
                result += word1[i];
            }
            if (i < len2) {
                result += word2[i];
            }
        }

        return result;
    }
};