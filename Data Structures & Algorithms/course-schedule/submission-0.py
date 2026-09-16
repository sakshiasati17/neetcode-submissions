from typing import List
from collections import defaultdict

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        graph = defaultdict(list)

        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(course):
            if states[course] == VISITED:
                return True

            if states[course] == VISITING:
                return False

            states[course] = VISITING

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False

            states[course] = VISITED
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True