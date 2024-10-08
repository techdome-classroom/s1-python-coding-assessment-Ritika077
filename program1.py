def num_islands(grid):
    if not grid:
        return 0

    # Dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Helper function to perform DFS
    def dfs(r, c):
        # If the current cell is out of bounds or is water ('W'), return
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
            return

        # Mark the current land ('L') cell as visited by turning it to 'W'
        grid[r][c] = 'W'

        # Perform DFS in the four possible directions (up, down, left, right)
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right

    # Initialize island count
    island_count = 0

    # Iterate through the grid
    for r in range(rows):
        for c in range(cols):
            # If we find an unvisited land cell, it's a new island
            if grid[r][c] == 'L':
                island_count += 1
                dfs(r, c)  # Mark all connected land cells

    return island_count
