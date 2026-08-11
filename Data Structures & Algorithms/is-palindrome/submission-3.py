class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = s.lower().replace(" ", "")
        i, j = 0, len(low) - 1

        while i < j:
            if low[j] in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                j -= 1
            elif low[i] in "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
                i += 1
            elif low[i] != low[j]:
                return False
            else:
                i += 1
                j -= 1
        return True