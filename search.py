import sys

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, start, end, cost):
        if start not in self.edges:
            self.edges[start] = []
        self.edges[start].append((end, cost))

def parse_input(filename):
    graph = {}
    nodes = {}
    origin = None
    goals = set()

    with open(filename, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):  # Ignore empty lines and comments
                continue

            if line.startswith("Nodes:"):
                section = "nodes"
                continue
            elif line.startswith("Edges:"):
                section = "edges"
                continue
            elif line.startswith("Origin:"):
                section = "origin"
                continue
            elif line.startswith("Destinations:"):
                section = "goals"
                continue

            if section == "nodes":
                parts = line.split(":")
                node_id = int(parts[0].strip())  # Ensure node ID is an integer
                coords = tuple(map(int, parts[1].strip(" ()").split(",")))  # Clean and extract coordinates
                nodes[node_id] = coords

            elif section == "edges":
                parts = line.split(":")
                edge_nodes = tuple(map(int, parts[0].strip(" ()").split(",")))  # Extract nodes
                cost = int(parts[1].strip())  # Extract cost
                if edge_nodes[0] not in graph:
                    graph[edge_nodes[0]] = []
                graph[edge_nodes[0]].append((edge_nodes[1], cost))

            elif section == "origin":
                origin = int(line.strip())

            elif section == "goals":
                goals = set(map(int, line.split(";")))

    return graph, nodes, origin, goals

def dfs(graph, start, goals):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue
        visited.add(node)
        nodes_expanded += 1

        if node in goals:
            return node, nodes_expanded, path  # Goal found

        if node in graph:  # Fix: Access graph directly, not graph.edges
            for neighbor, _ in sorted(graph[node], reverse=True):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, nodes_expanded, []  # No valid path found

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> DFS")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()

    if method != "DFS":
        print("This script currently only supports DFS.")
        sys.exit(1)

    graph, nodes, origin, goals = parse_input(filename)
    goal, nodes_expanded, path = dfs(graph, origin, goals)

    print(f"{filename} {method}")
    if path:
        print(f"{goal} {nodes_expanded}")
        print(" → ".join(map(str, path)))
    else:
        print("No path found.")