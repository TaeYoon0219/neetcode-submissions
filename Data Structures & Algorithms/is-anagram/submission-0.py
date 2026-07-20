class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checked1 = sorted(s)
        checked2 = sorted(t)
        if checked1 == checked2:
            return True
        else:
            return False
        
