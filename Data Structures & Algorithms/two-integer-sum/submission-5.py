class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            numMap[nums[i]] = i

        for i, num in enumerate(nums):
            if target - num in numMap and numMap[target - num] != i:
                return [i, numMap[target - num]]

        return []