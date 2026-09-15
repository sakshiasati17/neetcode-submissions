from collections import Counter, deque
import heapq
from typing import List


class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = []

        for task, count in freq.items():
            heapq.heappush(heap, -count)

        cooldown = deque()
        time = 0

        while heap or cooldown:

            while cooldown and cooldown[0][0] <= time:
                available_time, count = cooldown.popleft()
                heapq.heappush(heap, count)

            if heap:
                count = heapq.heappop(heap)
                count += 1

                if count != 0:
                    next_available_time = time + n + 1
                    cooldown.append((next_available_time, count))

            time += 1

        return time