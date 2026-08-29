class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_fir = sorted(s)
        sorted_sec = sorted(t)
        if sorted_fir == sorted_sec:
            return True
        return False    
        