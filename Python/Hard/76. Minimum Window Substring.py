class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        char_count_t, window = defaultdict(int), defaultdict(int)

        for char in t:
            char_count_t[char] += 1

        chars_needed, chars_have = len(char_count_t), 0
        result, result_len = [-1, 1], float("infinity")
        left_ptr = 0

        for right_ptr, current_char in enumerate(s):
            window[current_char] += 1

            if current_char in char_count_t and window[current_char] == char_count_t[current_char]:
                chars_have += 1

            while chars_have == chars_needed:
                current_len = right_ptr - left_ptr + 1

                if current_len < result_len:
                    result = [left_ptr, right_ptr]
                    result_len = current_len

                window[s[left_ptr]] -= 1

                if s[left_ptr] in char_count_t and window[s[left_ptr]] < char_count_t[s[left_ptr]]:
                    chars_have -= 1

                left_ptr += 1

        left, right = result
        return s[left: right + 1] if result_len != float("infinity") else ""
