def count_paths(input_string):
    # Parse the input string to create the grid and record the locations of A, B, and x
    rows = input_string.strip().split('\n')
    n_rows = len(rows)
    n_cols = len(rows[0].split())
    grid = [[rows[i].split()[j] for j in range(n_cols)] for i in range(n_rows)]
    a_row, a_col = None, None
    b_row, b_col = None, None
    x_locs = set()
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == 'A':
                a_row, a_col = i, j
            elif grid[i][j] == 'B':
                b_row, b_col = i, j
            elif grid[i][j] == 'x':
                x_locs.add((i, j))
    
    # Define a recursive function to count paths from the current location to B
    def count_paths_helper(row, col, visited):
        # Base cases:
        # - If the current location is out of bounds, return 0
        # - If the current location is equal to B, check that all non-x points have been visited
        #   and return 1 if they have, or 0 if they haven't
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return 0
        if row == b_row and col == b_col:
            if visited == set([(i, j) for i, j in x_locs]):
                return 1
            else:
                return 0
        
        # Recursive case:
        # - If the current location is equal to A, only consider neighbors to the right or down
        # - If the current location is not equal to A, consider all neighbors
        # - For each neighbor that is not an x and has not been visited, recursively count
        #   paths starting from that neighbor and add the results together
        if row == a_row and col == a_col:
            return count_paths_helper(row, col+1, visited) + count_paths_helper(row+1, col, visited)
        else:
            num_paths = 0
            for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_row, next_col = row + d_row, col + d_col
                if (next_row, next_col) not in x_locs and (next_row, next_col) not in visited:
                    num_paths += count_paths_helper(next_row, next_col, visited.union([(next_row, next_col)]))
            return num_paths
    
    # Call the recursive helper function starting from A with an empty set of visited points
    return count_paths_helper(a_row, a_col, set())
