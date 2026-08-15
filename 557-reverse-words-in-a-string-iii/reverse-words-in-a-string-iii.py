class Solution(object):
    def reverseWords(self, s):
        lst=s.split()
        nlst=[]
        string=''
        for i in lst:
            i=i[::-1]
            string+=i
            string+=' '
        string=string[0:-1]
        return string


        