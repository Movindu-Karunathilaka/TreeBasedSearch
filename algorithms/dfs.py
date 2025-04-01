def dfs(graph, start, goals):
    stack = [(start, [start])]
    visited = set()
    number_of_nodes = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue
        visited.add(node)
        number_of_nodes += 1

        if node in goals:
            return node, number_of_nodes, path  # Goal found

        if node in graph:  # Fix: Access graph directly, not graph.edges
            for neighbor, _ in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, number_of_nodes, []  # No valid path found