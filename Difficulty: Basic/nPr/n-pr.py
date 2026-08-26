class Solution:
    def nPr(self, n: int, r: int) -> int:
        # code here
        ans=1
        for i in range(r):
            ans=ans*(n-i)
        return ans