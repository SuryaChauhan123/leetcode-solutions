class Solution(object):
    def maximumWealth(self, accounts):
        lst=[]
        for i in accounts:
            money=0
            for j in i:
                money+=j
            lst.append(money)
        return max(lst)
            
        