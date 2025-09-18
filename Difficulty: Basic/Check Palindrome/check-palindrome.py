def isPalindrome(s):
    #code here
    s = s.lower()              
    return s == s[::-1]        