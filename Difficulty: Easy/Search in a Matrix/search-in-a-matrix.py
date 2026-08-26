class Solution:
    def searchMatrix(self, mat, x): 
    	# code her
    	for i in range(len(mat)):
    	    for j in range(len(mat[i])):
    	        if mat[i][j]==x:
    	            return True
        return False
