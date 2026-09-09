class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,x in enumerate(nums):
            ans=target-x
            if ans in seen:
                return [seen[ans],i]
            seen[x]=i