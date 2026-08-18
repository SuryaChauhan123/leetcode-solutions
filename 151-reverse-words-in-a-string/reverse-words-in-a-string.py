class Solution(object):
    def reverseWords(self, s):
        splt=s.split()
        ans=''
        for i in splt[::-1]:
            ans+=i
            ans+=' '
        return ans[0:-1]


        