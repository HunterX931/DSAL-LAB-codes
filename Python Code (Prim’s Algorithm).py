Python Code (Prim’s Algorithm)



import heapq

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost      # Cost from start to current node
        self.h_cost = h_cost      # Heuristic cost to goal
        self.f_cost = g_cost + h_cost
        self.parent = parent

    def __lt__(self, other):
        # Required for heapq to compare nodes
        return self.f_cost < other.f_cost

def a_star_search(maze, start, goal):
    open_list = []
    closed_set = set()
    cost_so_far = {start: 0}

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.position == goal:
            return reconstruct_path(current_node)

        closed_set.add(current_node.position)

        for neighbor_pos in get_neighbors(maze, current_node.position):
            if neighbor_pos in closed_set:
                continue

            g_cost = current_node.g_cost + 1  # Assuming uniform movement cost
            h_cost = heuristic(neighbor_pos, goal)

            # If this path is better or neighbor not visited yet
            if neighbor_pos not in cost_so_far or g_cost < cost_so_far[neighbor_pos]:
                cost_so_far[neighbor_pos] = g_cost
                neighbor_node = Node(neighbor_pos, g_cost, h_cost, current_node)
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found

def heuristic(pos1, pos2):
    # Manhattan distance
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(maze, position):
    neighbors = []
    row, col = position
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '#':
            neighbors.append((r, c))
    return neighbors

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]  # Reverse to get path from start to goal

# Example usage:
if __name__ == "__main__":
    maze = [
        ['S', '.', '#', '.'],
        ['.', '.', '#', '.'],
        ['.', '.', '.', 'G']
    ]
    start = (0, 0)
    goal = (2, 3)
    path = a_star_search(maze, start, goal)
    print("Path found:" if path else "No path found.")
    print(path)
