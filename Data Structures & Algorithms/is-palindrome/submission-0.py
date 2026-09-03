class Solution:
    def isPalindrome(self, s: str) -> bool:

        first_char ,last_char= 0, len(s)-1
        while first_char < last_char : 
            while first_char < last_char  and not self.alphaNum(s[first_char]):
                first_char += 1
            while last_char > first_char  and not self.alphaNum(s[last_char]):
                last_char -= 1     
            if s[first_char].lower() != s[last_char].lower():
                return False
            first_char += 1 
            last_char -= 1    
        return True        








    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))