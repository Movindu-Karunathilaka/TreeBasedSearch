import heapq

def greedy_bfs(graph, start, goals):
    pq = [(0, start)]  # Priority queue (h(n), node)
    came_from = {}  # Path tracking
    visited = set()
    number_of_nodes = 0

    while pq:
        _, node = heapq.heappop(pq)
        if node in visited:
            continue

        visited.add(node)
        number_of_nodes += 1

        if node in goals:
            return node, number_of_nodes, reconstruct_path(came_from, node)

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (0, neighbor))  # Greedy BFS only uses heuristic
                came_from[neighbor] = node

    return None, number_of_nodes, []  # No path found

def reconstruct_path(came_from, node):
    path = [node]
    while node in came_from:
        node = came_from[node]
        path.append(node)
    return path[::-1]  # Reverse for correct order
