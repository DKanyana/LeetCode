
def isPalindrome(self, x):
        copyX = x
        revnum = 0
        while x > 0:
            revnum = revnum*10 + x%10
            x = x//10
        return copyX == revnum
        
