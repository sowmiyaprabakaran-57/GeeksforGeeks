import math

class Solution:
    def jugglerSequence(self, n):
        seq = []
        while n != 1:
            seq.append(n)
            if n % 2 == 0:  
                n = math.isqrt(n)   
            else:  
                n = int(math.floor(n ** 1.5)) 
        seq.append(1)  
        return seq
