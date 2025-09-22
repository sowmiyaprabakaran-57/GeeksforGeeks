class Solution:
    def decToBinary(self, n):
        # code here
        if n==0:
            return "0"
        binary=""
        while n>0:
            remainder =n%2
            binary=str(remainder)+binary
            n=n//2
        return binary