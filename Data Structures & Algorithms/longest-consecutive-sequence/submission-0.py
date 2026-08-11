class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if n-1 not in numSet:
                length = 0
                current = 0
                while (n+ length) in numSet:
                    length += 1
                    current += 1
                if current > longest:
                    longest = current
        return longest