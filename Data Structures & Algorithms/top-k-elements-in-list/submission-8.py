class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        num_map = defaultdict(int)
        res = []

        for num in nums:
            num_map[num] += 1
        
        for num, freq in num_map.items():
            bucket[freq].append(num)

        for i in range(len(bucket) -1, 0, -1):
           for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
