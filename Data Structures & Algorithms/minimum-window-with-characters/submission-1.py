from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        first=Counter()
        second=Counter(t)
        left=0
        have=0
        min_len = float("inf")
        ans=""
        required=len(second)
        for right in range(len(s)):
            first[s[right]]+=1
            if s[right] in second and first[s[right]]==second[s[right]]:
                have+=1
            while have == required:
                if right-left+1<min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]
                first[s[left]] -= 1

                if s[left] in second and first[s[left]] < second[s[left]]:
                    have -= 1

                left += 1
        return ans




            
            
                