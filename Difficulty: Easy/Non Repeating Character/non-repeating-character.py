class Solution:
    def nonRepeatingChar(self,s):
        #code here
      #  k=[]
      # for i in range(len(s)):
      #     if s[i] in k:
      #         k.remove(s[i])
      #     k.append(s[i])
      # if k==[]:
      #     return "-1"
      # else:
      #     return k[0]
        count={}
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in s:
            if count[ch]==1:
                return ch
        return "$"