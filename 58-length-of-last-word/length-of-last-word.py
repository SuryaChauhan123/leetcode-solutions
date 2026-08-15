class Solution(object):
    def lengthOfLastWord(self, s):
        lst=s.split()
        length=len(lst[-1])
        return length
        