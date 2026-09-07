class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        res = []
        for i in nums:
            nums_map[i] = nums_map.get(i,0)+1
        max_val = float('-inf')
        for i in range(k):
            for key,val in nums_map.items():
                if val>max_val:
                    max_val = val
                    max_key = key
            res.append(max_key)
            nums_map.pop(max_key)
            max_val = float('-inf')
            max_key = 0
        return res