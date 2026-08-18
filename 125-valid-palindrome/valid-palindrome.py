class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        ans=''
        for i in s:
            if i.isalpha() or i.isnumeric():
                ans+=i
        if ans==ans[::-1]:
            return True
        else:
            return False

        