class Solution(object):
    def isPalindrome(self, x):
        
        if x<0:
            return False
        
        else:
            num=x
            last=0
            ans=0
            while num>0:
                last=num%10
                ans+=last*pow(10,len(str(num))-1)
                num=num//10
            if ans==x:
                return True
            else: 
                return False
