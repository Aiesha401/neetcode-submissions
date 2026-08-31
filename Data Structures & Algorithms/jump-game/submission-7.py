class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bottle = 'empty'
        for i,j in enumerate(nums):
            if bottle=='empty':
                bottle=j
                if bottle==0 and i!=len(nums)-1:
                    return False
                continue
            bottle-=1
            if bottle<j:
                bottle=j
            if (j==0 and bottle==0) and i!=len(nums)-1:
                return False
        return True
            