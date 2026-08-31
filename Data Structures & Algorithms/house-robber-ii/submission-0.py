class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def res(arr):
            if len(arr)==1:
                return arr[0]
            ans = [0]*len(arr)
            ans[0]=arr[0]
            ans[1]=max(arr[1],ans[0])
            for i in range(2,len(arr)):
                ans[i]=max(ans[i-2]+arr[i],ans[i-1])
            print(ans)
            return ans[-1]
        a = res(nums[1:])
        b = res(nums[:len(nums)-1])
        print(a,b)
        return max(a,b)
        