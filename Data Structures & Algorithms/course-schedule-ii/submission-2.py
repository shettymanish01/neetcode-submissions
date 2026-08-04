class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = {i:[] for i in range(numCourses)}
        res = []
        visited = set()
        visiting = set()
        for cur, pre in prerequisites:
            course_map[cur].append(pre)

        def dfs(c):
            if c in visiting:
                return False

            if c in visited:
                return True
            

            visiting.add(c)
            for pre in course_map[c]:
                if not dfs(pre):
                    return False
            res.append(c)
            visited.add(c)
            visiting.remove(c)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res