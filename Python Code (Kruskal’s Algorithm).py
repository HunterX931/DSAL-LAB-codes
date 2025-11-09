def is_connected(graph, u, v, visited):
    if u == v:
        return True
    visited[u] = True
    for neighbor in graph[u]:
        if not visited[neighbor] and is_connected(graph, neighbor, v, visited):
            return True
    return False

def main():
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of edges: "))

    edges = []
    # Create adjacency matrix and list
    adj_matrix = [[0] * n for _ in range(n)]
    adj_list = [[] for _ in range(n)]

    print("Enter edges (u v w):")
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        # Fill adjacency matrix (undirected)
        adj_matrix[u][v] = w
        adj_matrix[v][u] = w
        # Fill adjacency list
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # Print adjacency matrix
    print("\nAdjacency Matrix:")
    print("   ", end="")
    for i in range(n):
        print(f"{i:3}", end="")
    print()
    for i in range(n):
        print(f"{i:2} ", end="")
        for j in range(n):
            print(f"{adj_matrix[i][j]:3}", end="")
        print()

    # Print adjacency list
    print("\nAdjacency List:")
    for i in range(n):
        neighbors = " ".join(f"({v}, {w})" for v, w in adj_list[i])
        print(f"{i} -> {neighbors}")


    # Step 2: Build MST using DFS connectivity check
    edges.sort()
    graph = [[] for _ in range(n)]  # MST graph
    totalWeight = 0
    count = 0

    print("\nMinimum Spanning Tree (Simple):")
    for w, u, v in edges:
        visited = [False] * n
        if not is_connected(graph, u, v, visited):
            print(f"{u} -- {w} --> {v}")
            totalWeight += w
            graph[u].append(v)
            graph[v].append(u)
            count += 1
            if count == n - 1:
                break

    print("Total weight of MST:", totalWeight)

if __name__ == "__main__":
    main()
