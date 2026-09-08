class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        results=[]
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        sorted_nums = sorted(counts, key=lambda x: counts[x], reverse=True)
        return sorted_nums[:k]

        
            
                    
        