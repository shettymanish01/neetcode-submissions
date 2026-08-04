class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        hashmap = {i: [] for i in range(numCourses)}
        for c, r in prerequisites:
            hashmap[c].append(r)

        def takeCourse(course):
            if course in visited:
                print(visited)
                return False
            if hashmap[course] == []:
                return True
            
            visited.add(course)

            for co in hashmap[course]:
                    if not takeCourse(co):
                        return False
            visited.remove(course)
            hashmap[course] = []
            return True

        for i in range(numCourses):
            if not takeCourse(i):
                return False

        return True
            
