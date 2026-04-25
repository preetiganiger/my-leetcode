class Solution(object):
   
    def reverse(self,x):
        last=0
        rev=0
        count=0
        num=abs(x)
        l=len(str(num))-1
        while(num>0):
            last =num%10
            rev+=last*pow(10,l)
            l -= 1
            num = num//10
        if rev>pow(2,31) or rev<-pow(2,31):
            return 0
        elif x>0:
          return rev
        else:
            return -rev
        