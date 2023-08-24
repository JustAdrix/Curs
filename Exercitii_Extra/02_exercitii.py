# class Solution:
#     def searchWord(self, grid, word):
#         self.grid = grid
#         self.word = word
#         n, m = len(self.grid), len(self.grid[0])
#         result = []
#
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#
#         for self.x in range(self.n):
#             for self.y in range(self.m):
#                 for self.direction in directions:
#                     visited = [[False for _ in range(m)] for _ in range(n)]
#                     if dfs(self.grid, word, x, y, direction, visited):
#                         result.append((x, y))
#
#         return sorted(result)
#
#     def is_valid(self,x, y, n, m):
#         self.x = x
#         self.y = y
#         self.n = n
#         self.m = m
#
#         return 0 <= self.x < self.n and 0 <= self.y < self.m
#
#     def dfs(self, direction, visited):
#         self.direction = direction
#         self.visited = visited
#         self.n = len(self.grid)
#         self.m = len(self.grid[0])
#         self.dx, self.dy = self.direction
#
#         for char in self.word:
#             if not is_valid(self.x, self.y, self.n, self.m) or self.grid[self.x][self.y] != char or self.visited[self.x][self.y]:
#                 return False
#             self.x += self.dx
#             self.y += self.dy
#
#         return True

# grid = {{a, b, c}, {d, r, f}, {g, h, i}},
# ord = "abc"


# def is_valid(x, y, n, m):
#     return 0 <= x < n and 0 <= y < m


# def dfs(grid, word, x, y, direction, visited):
#     n = len(grid)
#     m = len(grid[0])
#     dx, dy = direction
#
#     for char in word:
#         if not is_valid(x, y, n, m) or grid[x][y] != char or visited[x][y]:
#             return False
#         x += dx
#         y += dy
#
#     return True


# def find_word_in_grid(grid, word):
    # n, m = len(grid), len(grid[0])
    # result = []
    #
    # directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    #
    # for x in range(n):
    #     for y in range(m):
    #         for direction in directions:
    #             visited = [[False for _ in range(m)] for _ in range(n)]
    #             if dfs(grid, word, x, y, direction, visited):
    #                 result.append((x, y))
    #
    # return sorted(result)
n = 5
result =0

for i in range(n+1):
    result +=i
print(result)


# Example usage
# grid = [
#     ['a', 'b', 'c', 'd'],
#     ['e', 'f', 'g', 'h'],
#     ['i', 'j', 'k', 'l'],
#     ['m', 'n', 'o', 'p']
# ]
# word = "ejo"
# print(find_word_in_grid(grid, word))  # Output: [(1, 2), (2, 1), (2, 2)]
