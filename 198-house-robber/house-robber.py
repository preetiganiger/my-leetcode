"""class Solution(object):

    def rob(self, nums):
       n= len(nums)
       prev=nums[0]
       prev2=0
       
      for i in range (1,n):
            if n == 1:
              return nums[0]
            if i>1:
                pick= nums[i]+prev2
            else: 
                    pick= nums[i]
            notpick = 0+prev
            curr = max(pick,notpick)
                
            prev2=prev
            prev=curr
      return prev
    
"""
class Solution(object):
    def rob(self, nums):
        # Handle empty input array safely
        if not nums:
            return 0
        
        n = len(nums)
        # Handle single-house scenario immediately
        if n == 1:
            return nums[0]
            
        prev = nums[0]
        prev2 = 0
        
        for i in range(1, n):
            # If i > 1, we can add the current house loot to prev2
            if i > 1:
                pick = nums[i] + prev2
            else:
                pick = nums[i]
                
            notpick = prev
            curr = max(pick, notpick)
            
            # Slide the dynamic programming state window forward
            prev2 = prev
            prev = curr
            
        return prev

        