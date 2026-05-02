class Solution(object):
    def mergeAlternately(self, word1, word2):
        w1=list(word1)
        w2=list(word2)
        loop=min(len(word1),len(word2))
        merge=[]
        for i in range(loop):
            merge.append(w1[i])
            merge.append(w2[i])
        merge.append(word1[loop:])
        merge.append(word2[loop:])
           
        return "".join(merge)
        