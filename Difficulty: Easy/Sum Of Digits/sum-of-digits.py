class Solution:
    def sumOfDigits(self, n):
        # code here
        s=0
        for i in str(n):
            s+=int(i)
        return s
            