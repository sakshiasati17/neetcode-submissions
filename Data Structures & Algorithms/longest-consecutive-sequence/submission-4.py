class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:              # handle empty list
            return 0
        nums.sort()
        curr=1
        longg=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
            else:
                curr=1
            if curr > longg:
                longg=curr
        return longg
            
            