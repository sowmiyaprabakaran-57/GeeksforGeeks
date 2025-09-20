class Solution:
    def firstRepeated(self,arr):
        # code here 
        n=len(arr)
        freq={}
        for num in arr:
            freq[num]=freq.get(num,0)+1
        for i in range(n):
            if freq[arr[i]]>1:
                return i+1
        return -1