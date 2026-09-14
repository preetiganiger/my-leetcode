'''class Solution(object):
    def containsDuplicate(self, nums)-> bool:
        y=sorted(nums)
        for i in range(0,len(y)):
            
            if y[i]==y[i+1]:
                return True
        return False
class Solution(object):
    def containsDuplicate(self, nums):
    
        y = sorted(nums)

        for i in range(0, len(y) - 1):
            if y[i] == y[i + 1]:
                return True

        return False'''

class Solution(object):
    def containsDuplicate(self, nums):
        y = sorted(nums)

        for i in range(len(y) - 1):
            if y[i] == y[i + 1]:
                return True

        return False    