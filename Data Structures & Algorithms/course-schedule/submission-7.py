class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return False

            visited.add(node)
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visited.remove(node)
            return True

            
        for course, _ in prerequisites:
            if not dfs(course):
                return False
        return True