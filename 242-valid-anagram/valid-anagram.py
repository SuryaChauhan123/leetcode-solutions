class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            sorts=''.join(sorted(s))
            sortt=''.join(sorted(t))
            if sorts.lower()==sortt.lower():
                return True
            else:
                return False
        else:
            return False
        