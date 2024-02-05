class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> charCount;
        for (char c : s) {
            charCount[c]++;
        }
        auto cmp = [](pair<int, char>& a, pair<int, char>& b) {
            return a.first < b.first;
        };
        priority_queue<pair<int, char>, vector<pair<int, char>>, decltype(cmp)> maxHeap(cmp);

        for (auto it = charCount.begin(); it != charCount.end(); ++it) {
            maxHeap.push({it->second, it->first});
        }

        string result = "";

        while (maxHeap.size() >= 2) {
            pair<int, char> first = maxHeap.top();
            maxHeap.pop();
            pair<int, char> second = maxHeap.top();
            maxHeap.pop();
            result += first.second;
            result += second.second;

            if (first.first > 1) {
                maxHeap.push({first.first - 1, first.second});
            }
            if (second.first > 1) {
                maxHeap.push({second.first - 1, second.second});
            }
        }
        if (!maxHeap.empty()) {
            result += maxHeap.top().second;
        }

        return result.length() == s.length() ? result : "";
    }
};