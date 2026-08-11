class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS = sorted(s)
        sortT = sorted(t)

        if sortS == sortT:
            return True
        else:
            return False
        