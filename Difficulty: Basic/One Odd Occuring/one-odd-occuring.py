class Solution:
    def getOddOccurrence(self, arr):
        # code here 
        count=0
        for i in arr:
            count^=i
        return count
            