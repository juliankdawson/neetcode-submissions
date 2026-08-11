class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s.lower()

        left, right, curr = (0, 0, 0)
        letters, res = [], 0

        if s == "":
            return 0

        if s == " ":
            return 1

        while left < len(s) and right < len(s):
            if s[right] in letters:
                letters = []
                left += 1
                right = left
                curr = 0
            else:
                letters.append(s[right])
                curr += 1
                right += 1
                
            res = max(res, curr)

        return res