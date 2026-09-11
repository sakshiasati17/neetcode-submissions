from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k=len(s1)
        if len(s2)<k:
            return False
        need = Counter(s1)
        window=Counter(s2[:k])
        if need==window:
            return True
        for right in range(k,len(s2)):
            window[s2[right]]+=1
            window[s2[right - k]] -= 1
            if window[s2[right - k]] == 0:
                del window[s2[right - k]]
            if window == need:
                return True
        return False


        

        