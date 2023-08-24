class Solution:
    def is_valid(self, x, y, n, m):
        self.x = x
        self.y = y
        self.n = n
        self.m = m
        return 0 <= self.x < self.n and 0 <= self.y < self.m


    def dfs(self, direction, visited):
        self.direction = direction
        self.visited = visited
        self.n = len(self.grid)
        self.m = len(self.grid[0])
        self.dx, self.dy = self.direction

        for char in self.word:
            if not is_valid(self.x, self.y, self.n, self.m) or self.grid[self.x][self.y] != char or self.visited[self.x][
                self.y]:
                return False
            self.x += self.dx
            self.y += self.dy

        return True

    def searchWord(self, grid, word):
            self.grid = grid
            self.word = word



            self.n, self.m = len(self.grid), len(self.grid[0])
            result = []

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

            for self.x in range(self.n):
                for self.y in range(self.m):
                    for self.direction in directions:
                        visited = [[False for _ in range(m)] for _ in range(n)]
                        if dfs(self.grid, self.word, self.x, self.y, self.direction, self.visited):
                            result.append((x, y))

            return sorted(result)


a = Solution()
print(a)