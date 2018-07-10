"""

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

"""

def isPalindrome(self, x):
        copyX = x
        revnum = 0
        while x > 0:
            revnum = revnum*10 + x%10
            x = x//10
        return copyX == revnum
        
