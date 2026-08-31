class Solution(object):
    def removeStars(self, s):
        ans=[]
        for i in s:
            if i!='*':
                ans.append(i)
            else:
                ans.pop()
        return ''.join(ans[::1])
        