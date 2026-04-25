//Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
//Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

//mycode
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
 */ Approach
Sign Handling: Check if the input x is positive or negative.
String Conversion & Reversal:
If x>0, convert it to a string and reverse it using the slicing operator [::-1].
If x<0, extract the magnitude (the part after the negative sign), reverse it, and then re-apply the negative sign.
Overflow Protection: Before returning, check if the reversed integer rev_s falls outside the 32-bit signed integer boundaries:
Lower Bound: −2 
31
 
Upper Bound: 2 
31
 −1
Edge Cases: If the result overflows or the input is 0, the function returns 0.
Complexity
Time complexity: O(log(n))
Space complexity: O(log(n))
Code /*

class Solution(object):
    def reverse(self, x):
        rev_s = 0
        if x > 0:
            str_x = str(x)
            rev_s = int(str_x[::-1])
        elif x < 0:
            str_x = str(x)
            str_x = str_x[1:]
            rev_s = -1 * int(str_x[::-1])
        if x == 0 or rev_s < (-1* pow(2,31)) or rev_s > (pow(2,31) - 1):
            return 0
        return rev_s
