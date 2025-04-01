import heapq
from parse import parse_file

def greedy_best_first_search(graph, start, goals, nodes):
    # Open list (priority queue), closed set (visited nodes)
    pq = [(heuristic(start, goals, nodes), start)]  # (h(n), node)
    came_from = {}  # Tracing back the path
    visited = set()

    while pq:
        _, node = heapq.heappop(pq)  # Get best node (smallest h(n))
        if node in visited:
            continue  # Skip stuff we've seen
        
        visited.add(node)
        if node in goals:
            return reconstruct_path(came_from, node), len(visited)  # Done, return path & expanded count

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic(neighbor, goals, nodes), neighbor))
                came_from[neighbor] = node  # Track the path

    return None, len(visited)  # No path found

def heuristic(node, goals, nodes):
    return min(manhattan_distance(nodes[node], nodes[g]) for g in goals)  # Pick closest goal

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Simple distance calc

def reconstruct_path(came_from, node):
    path = []
    while node in came_from:
        path.append(node + 1)  # Convert 0-index to 1-index
        node = came_from[node]
    path.append(node + 1)
    return path[::-1]  # Reverse for correct order

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    nodes, edges, origin, destinations = parse_file(filename)
    path, expanded = greedy_best_first_search(edges, origin, destinations, nodes)
    if path:
        print(len(path), expanded)  # Nodes in path, nodes expanded
        print(" → ".join(map(str, path)))  # Show path as 1 → 2 → 3
    else:
        print("No path found")
