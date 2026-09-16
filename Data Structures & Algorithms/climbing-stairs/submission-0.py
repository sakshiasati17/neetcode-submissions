class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        previous_two = 1  
        previous_one = 2  

        for stair in range(3, n + 1):
            current = previous_one + previous_two
            previous_two = previous_one
            previous_one = current

        return previous_one
            