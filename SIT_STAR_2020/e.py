
import sys
from functools import lru_cache
sys.setrecursionlimit(10000)
n,k = map(int,input().split())
sys.setrecursionlimit(1500000)
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

count = 0
def dfs(grid, fa, i, j,count):
    # if not in grid x
    # if not in grid y
    #
    if i >= len(grid) or i < 0 or j < 0 or j >= len(grid[i]) or grid[i][j] == '.':
        return 0
    
    grid[i][j] = '.'
    fa[i][j] = letters[count]

    dfs(grid,fa,i + 1, j,count)
    dfs(grid,fa,i - 1, j,count)
    dfs(grid,fa,i, j + 1,count)
    dfs(grid,fa,i, j - 1,count)
    return 1

def numIslands(grid, fa) -> int:
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                dfs(grid,fa,i,j,count)
                count += 1
    
    return count

temp_n = n
temp_k = k

nums = []

fa = [['.'] * k for _ in range(n)]

while temp_n != 0:
    inp = list(input())
    nums.append(inp)
    temp_n -= 1

numIslands(nums,fa)

for i in fa:
    print(''.join([str(e) for e in i]))