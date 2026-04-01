class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        neighbors = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(x, y, visited):
            if (x, y) in visited:
                return

            visited.add((x, y))

            for add_x, add_y in neighbors:
                new_x = x + add_x
                new_y = y + add_y
                if min(new_x, new_y) >= 0 and new_x < len(heights) and new_y < len(heights[0]) and heights[x][y] <= heights[new_x][new_y]:
                    dfs(new_x, new_y, visited)

        
        # leftmost colum, rightmost column
        for x in range(len(heights)):
            dfs(x, 0, pacific)
            dfs(x, len(heights[0]) - 1, atlantic)

        # first row, last row
        for y in range(len(heights[0])):
            dfs(0, y, pacific)
            dfs(len(heights) - 1, y, atlantic)

        answer = []
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if (x, y) in pacific and (x, y) in atlantic:
                    answer.append([x, y])
        return answer
        
