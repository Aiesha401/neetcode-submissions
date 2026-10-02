class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if (target+total) %2 !=0 or total+target<0:
            return 0
        s1 = (target + total)//2
        def count_subset_sum(nums,target):
            t = [[-1]*(target+1) for _ in range(len(nums)+1)]
            for i in range(len(nums)+1):
                for j in range(target+1):
                    if i == 0:
                        t[i][j] = 0
                    if j == 0:
                        t[i][j] = 1
            
            for i in range(1,len(nums)+1):
                for j in range(target+1):
                    if nums[i-1] <= j:
                        t[i][j] = t[i-1][j-nums[i-1]] + t[i-1][j]
                    else:
                        t[i][j] = t[i-1][j]
            
            return t[len(nums)][target]
        res = count_subset_sum(nums,s1)
        return res

        