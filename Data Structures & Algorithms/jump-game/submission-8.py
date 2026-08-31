class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bottle = nums[0]
        if bottle==0 and len(nums)>1:
            return False
        for i,j in enumerate(nums):
            if i==0:
                continue
            bottle-=1
            if bottle<j:
                bottle=j
            if (j==0 and bottle==0) and i!=len(nums)-1:
                return False
        return True
            