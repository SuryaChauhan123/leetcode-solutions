class Solution(object):
    def intersection(self, nums1, nums2):
        nlst=[]
        ans=len(nums1)>len(nums2)
        if ans==True:
            for i in nums1:
                if i in nums2 and i not in nlst:
                    nlst.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in nlst:
                    nlst.append(i)
        return nlst
        