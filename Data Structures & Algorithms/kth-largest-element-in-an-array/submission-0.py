class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for num in nums:
            nums.sort(reverse=True)



            return nums[k - 1]
        