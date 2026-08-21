class Solution:
    def visibleBuildings(self, arr):
        # code here
        count=0
        max_h=0
        for i in range(len(arr)):
            if arr[i]>=max_h:
                count+=1
                max_h=arr[i]
        return count