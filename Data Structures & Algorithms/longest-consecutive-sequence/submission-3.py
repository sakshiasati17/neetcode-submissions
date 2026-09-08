class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:              # handle empty list
            return 0
        
        nums.sort()               # 1) sort
        longest = 1               # final answer
        curr_len = 1              # current streak

        n = len(nums)
        for i in range(1, n):
            # skip duplicates like [1,1,2,3]
            if nums[i] == nums[i - 1]:
                continue
            # consecutive → extend streak
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                # streak broke → reset
                curr_len = 1
            # update longest
            if curr_len > longest:
                longest = curr_len

        return longest
