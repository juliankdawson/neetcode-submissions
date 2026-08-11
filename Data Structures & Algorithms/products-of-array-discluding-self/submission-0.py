class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = ["#"] * len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if mul[i] == "#":
                        mul[i] = nums[j]
                    else:
                        mul[i] *= nums[j]
        return mul
        