class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case for an empty string t
        if t == "":
            return ""

        # Init Hashmaps for Sliding Window and Freq. of chars in T
        countT, window = {}, {}

        # Store char --> freq. (in countT)
        for c in t:
            countT[c] = 1 + countT.get(c, 0) #.get for edge case
        
        # Have: num chars from s in t
        # Need: num unique chars in t
        have, need = 0, len(countT)
        # Res: indicies of sstisfiying substring
        # Reslen: length of satisfying substring
        res, resLen = [-1, -1], float("infinity") #converts string/num --> num
        l = 0 #left pointer

        # Right pointer iterates through string s
        for r in range(len(s)):
            c = s[r] #current char
            window[c] = 1 + window.get(c, 0) # update slding window with freq.

            # If current char is in t and freq. is equal increment have
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # Logic to find min. substring by decrementing left pointer
            while have == need:
                # len(window) < resLen we need to update our result
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # decrement freq of char at left pointer by 1
                window[s[l]] -= 1

                # Check that char at left pointer and it's freq in window
                # is less than freq in T we decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # update left pointer
                l += 1

        # destructure pointers from res indicies
        l, r = res
        # return final substring or empty string if we didn't create one
        return s[l : r + 1] if resLen != float("infinity") else ""
