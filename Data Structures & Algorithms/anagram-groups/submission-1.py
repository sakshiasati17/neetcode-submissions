class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for x in strs:
            key="".join(sorted(x))
            if key in freq:
                freq[key].append(x)
            else:
                freq[key]=[x]
        return list(freq.values())

            