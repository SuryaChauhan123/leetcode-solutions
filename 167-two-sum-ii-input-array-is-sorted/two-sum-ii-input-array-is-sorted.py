class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        i=0
        j=n-1
        while i<j:
            sno=nums[i]+nums[j]
            if sno==target:
                return [i+1,j+1]
            elif sno>target:
                j-=1
            elif sno<target:
                i+=1
        return []
