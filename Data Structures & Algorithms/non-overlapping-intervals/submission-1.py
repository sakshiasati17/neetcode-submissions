class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        removed = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < previous_end:
                removed += 1
                previous_end = min(previous_end, end)
            else:
                previous_end = end

        return removed