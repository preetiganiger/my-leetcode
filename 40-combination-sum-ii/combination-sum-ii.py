'''class Solution(object):
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
        self.fun( candidates, target,index+1,sums,subset,result)
        subset.pop()
        sums=total
        self.fun(candidates, target,index+1,sums,subset,result)
    def combinationSum2(self, candidates, target):
       
        result=[]
        subset=[]
        self.fun(candidates, target,0,0,subset,result)
        return result'''
class Solution(object):
    def fun(self, candidates, target, index, subset, result):
        if target == 0:
            result.append(subset[:])
            return

        for i in range(index, len(candidates)):
            # Skip duplicates
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > target:
                break

            subset.append(candidates[i])

            # Move to the next index (cannot reuse the same element)
            self.fun(candidates, target - candidates[i], i + 1, subset, result)

            subset.pop()

    def combinationSum2(self, candidates, target):
        candidates.sort()
        result = []
        self.fun(candidates, target, 0, [], result)
        return result