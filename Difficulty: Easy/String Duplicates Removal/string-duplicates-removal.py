#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    seen=set()
	    result=[]
	    for char in s:
	        if char not in seen:
	            seen.add(char)
	            result.append(char)
	    return "".join(result)