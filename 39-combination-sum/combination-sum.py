class Solution(object):
    def fun(self, candidates, target,index,total,subset,result):
        if total==target:
            result.append(subset[:])
            return
        if index>= len(candidates):
            return 
        if total>target:
            return
        subset.append(candidates[index])
        sums= total+candidates[index]
        self.fun( candidates, target,index,sums,subset,result)
        subset.pop()
        sums=total
        self.fun(candidates, target,index+1,sums,subset,result)
        
    def combinationSum(self, candidates, target): 
        result=[]
        subset=[]
        self.fun(candidates, target,0,0,subset,result)
        return result
"""""
class Solution(object):

    def fun(self, candidates, target, index, total, subset, result):
        if total == target:
            result.append(subset[:]) 
            return

        if index >= len(candidates):
            return

        if total > target:
            return

        subset.append(candidates[index])
        self.fun(candidates, target, index, total + candidates[index], subset, result)

        subset.pop()

        self.fun(candidates, target, index + 1, total, subset, result)

    def combinationSum(self, candidates, target):
        result = []
        subset = []

        self.fun(candidates, target, 0, 0, subset, result)

        return result
        """