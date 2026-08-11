class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #value -> occur
        freq = [[] for i in range(len(nums) + 1)] #Index = freq[1] all nums ocurr once 

        #Build Hashmap
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n) #For given num insert into index of freq

        res = []
        #start at last index and insert all numbers with highest freq in decending order into array
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res