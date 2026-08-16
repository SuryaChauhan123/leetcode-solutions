class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even_num=[]
        odd_num=[]
        for i in nums:
            if i%2==0:
                even_num.append(i)
            else:
                odd_num.append(i)
        nlst=even_num+odd_num
        return nlst
        