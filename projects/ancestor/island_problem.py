from util import Stack
# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

# island_counter(islands) # returns 4

# Unweighted
# Undirected
# Cyclic

# Nodes are numbers, edges are connections between 1s

# 1. Is this a graphs problem?
# 2. Build the graph
# 3. Traverse the graph

# Visit each cell in the 2D array.
# When you come across a 1:
# Traverse it and mark all connected nodes as visited,
# Then increment a counter.


def get_island_neighbors(x, y, matrix):
    neighbors = []
    # Check north
    if y > 0 and matrix[y-1][x] == 1:
        neighbors.append((x, y-1))
    # Check south
    if y > len(matrix)-1 and matrix[y+1][x] == 1:
        neighbors.append((x, y+1))
    # Check east
    if x < len(matrix[0]) - 1 and matrix[y][x+1] == 1:
        neighbors.append((x+1, y))
    # Check west
    if x > 0 and matrix[y][x-1] == 1:
        neighbors.append((x-1, y))

    return neighbors


def dft_islands(start_x, start_y, matrix, visited):
    s = Stack()
    s.push((start_x, start_y))

    while s.size() > 0:

        vertex = s.pop()
        x = vertex[0]
        y = vertex[1]

        if not visited[y][x]:
            visited[y][x] = True

            for neighbor in get_island_neighbors(x, y, matrix):  # STUB
                s.push(neighbor)
    return visited


def island_counter(matrix):
    # Created a visited matrix with the same dimensions as islands matrix
    # Visit each cell in the 2d array...
        # If it has not been visited...
            # When you come across a 1
            # DFT it and mark all connected nodes as visited,
            # Then increment a counter
    visited = []
    matrix_height = len(matrix)
    matrix_width = len(matrix[0])
    for i in range(matrix_height):
        visited.append([False * matrix_width])
    # Create a counter, initialize to 0
    counter = 0
    # For each cell in 2D array...
    for x in range(matrix_width):
        for y in range(matrix_height):
            # If it has not been visited...
            if not visited[y][x]:
                if matrix[y][x] == 1:
                    visited = dft_islands(x, y, matrix, visited)  # STUB
                    counter += 1
    return counter


print(island_counter(islands))
