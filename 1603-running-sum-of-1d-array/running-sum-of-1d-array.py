class Solution(object):
    def runningSum(self, nums):
        count=0
        lst=[]
        for i in nums:
            count+=i
            lst.append(count)
        return lst