#User function Template for python3

class Solution:
    def isStrong(self, N):
        total=0
        temp=N
        while temp>0:
            digit=temp%10
            total+=math.factorial(digit)
            temp//=10
        if total==N:
            return 1
        else:
            return 0