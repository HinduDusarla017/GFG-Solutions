class Solution:
	def preGreaterEle(self, arr):
		# code here
		n=len(arr)
		pge=[-1]*n
		stack=[]
		for i in range(n):
		    while stack and stack[-1]<=arr[i]:
		        stack.pop()
		    if stack:
		        pge[i]=stack[-1]
		    stack.append(arr[i])
		return pge
		           