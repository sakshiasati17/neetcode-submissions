class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        sorted_list=sorted(freq.items(), key=lambda item: item[1],reverse=True)
        ans=[]
        for num, count in sorted_list:
            ans.append(num)
            if len(ans)==k:
                break
        return ans
                
                