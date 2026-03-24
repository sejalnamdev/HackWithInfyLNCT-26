def gridChallenge(grid):
    grid = [''.join(sorted(row)) for row in grid]
    return "YES" if all(grid[i][j] <= grid[i+1][j] 
                        for i in range(len(grid)-1) 
                        for j in range(len(grid[0]))) else "NO"