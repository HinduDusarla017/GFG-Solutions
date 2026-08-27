class Solution:
	def arraySum(self, arr):
   		# code here
        s=0
        for i in range(len(arr)):
            s+=arr[i]
        return s