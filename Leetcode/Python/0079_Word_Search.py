'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:


Input: board = 

[["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], 

word = "ABCCED"
Output: true
Example 2:


Input: board = 

[["A","B","C","E"]
["S","F","C","S"],
["A","D","E","E"]], 

word = "SEE"
Output: true
Example 3:


Input: board = 
[["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]], 

word = "ABCB"
Output: false
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, i):

            if i == len(word):
                return True
            if x >= len(board) or x < 0 or y >= len(board[0]) or y < 0 or board[x][y] != word[i]:
                return False
            temp = board[x][y]
            board[x][y] = "#"
            found = (
                    dfs(x + 1, y, i + 1) or
                    dfs(x - 1, y, i + 1) or
                    dfs(x, y + 1, i + 1) or
                    dfs(x, y - 1, i + 1)
                )
            board[x][y] = temp
            return found
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
            

        