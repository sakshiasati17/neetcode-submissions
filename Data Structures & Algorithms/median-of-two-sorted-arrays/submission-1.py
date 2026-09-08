class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s=nums1+nums2
        s.sort()
        n=len(s)
        if n % 2 == 1:
            mid = n // 2
            return float(s[mid])
        else:
            mid = n // 2
            return (s[mid - 1] + s[mid]) / 2


                

        