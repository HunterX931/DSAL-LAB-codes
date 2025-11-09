import heapq

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost  # Cost from start to current node
        self.h_cost = h_cost  # Heuristic cost from current node to goal
        self.f_cost = g_cost + h_cost  # Total cost
        self.parent = parent

    def __lt__(self, other):
        return self.f_cost < other.f_cost


def a_star_search(maze, start, goal):
    open_list = []
    heapq.heappush(open_list, Node(start, 0, heuristic(start, goal)))

    g_costs = {start: 0}  # Track best known g_cost for each position
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)
        current_pos = current_node.position

        if current_pos == goal:
            return reconstruct_path(current_node)

        if current_pos in closed_list:
            continue
        closed_list.add(current_pos)

        for neighbor_pos in get_neighbors(maze, current_pos):
            if neighbor_pos in closed_list:
                continue

            tentative_g_cost = current_node.g_cost + 1  # Assuming uniform move cost

            # Only consider this new path if it’s better
            if neighbor_pos not in g_costs or tentative_g_cost < g_costs[neighbor_pos]:
                g_costs[neighbor_pos] = tentative_g_cost
                h_cost = heuristic(neighbor_pos, goal)
                neighbor_node = Node(neighbor_pos, tentative_g_cost, h_cost, current_node)
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found


def heuristic(pos1, pos2):
    """Manhattan distance heuristic."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_neighbors(maze, position):
    neighbors = []
    row, col = position
    possible_moves = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for r, c in possible_moves:
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] != '#':
            neighbors.append((r, c))
    return neighbors


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]


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
    print("Path found:", path)
