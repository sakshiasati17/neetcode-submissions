class Solution:
    def rob(self, nums: List[int]) -> int:
        previous_two = 0
        previous_one = 0

        for money in nums:
            take = money + previous_two
            skip = previous_one

            current = max(take, skip)

            previous_two = previous_one
            previous_one = current

        return previous_one