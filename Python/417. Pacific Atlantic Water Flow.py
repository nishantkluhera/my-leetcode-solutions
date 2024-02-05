class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        M, N = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean):
            ocean.add((r, c))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + di, c + dj
                if 0 <= new_r < M and 0 <= new_c < N and heights[r][c] <= heights[new_r][new_c] and (new_r, new_c) not in ocean:
                    dfs(new_r, new_c, ocean)

        for r in range(M):
            dfs(r, 0, pacific)
            dfs(r, N-1, atlantic)

        for c in range(N):
            dfs(0, c, pacific)
            dfs(M-1, c, atlantic)

        return list(pacific & atlantic)             