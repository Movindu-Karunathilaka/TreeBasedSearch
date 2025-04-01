from pathlib import Path
import sys

# Import algorithms here
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra


def parse_input(filename):
    graph = {}
    nodes = {}
    origin = None
    goals = set()

    with open(filename, 'r') as file:
        section = None
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):  
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
                node_id = int(parts[0].strip())
                coords = tuple(map(int, parts[1].strip(" ()").split(",")))
                nodes[node_id] = coords

            elif section == "edges":
                parts = line.split(":")
                edge_nodes = tuple(map(int, parts[0].strip(" ()").split(",")))
                cost = int(parts[1].strip())
                if edge_nodes[0] not in graph:
                    graph[edge_nodes[0]] = []
                graph[edge_nodes[0]].append((edge_nodes[1], cost))

            elif section == "origin":
                origin = int(line.strip())

            elif section == "goals":
                goals = set(map(int, line.split(";")))

    return graph, nodes, origin, goals


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python search.py <filename> <algorithm>\nAvailable algorithms: DFS, Dijkstra")
        sys.exit(1)

    filename = sys.argv[1]
    method = sys.argv[2].upper()
    
    if not Path(filename).exists():
        print(f"Error: File '{filename}' does not exist. Make sure to have 'tests/' before file name")
        sys.exit(1)

    graph, nodes, origin, goals = parse_input(filename)

    if method == "DFS":
        goal, number_of_nodes, path = dfs(graph, origin, goals)
    elif method == "DIJKSTRA":
        goal, number_of_nodes, path = dijkstra(graph, origin, goals)
    else:
        print("Invalid algorithm")
        sys.exit(1)

    print(f"Filename: {filename} Method: {method}")
    if path:
        print(f"Goal: {goal} Total Nodes: {number_of_nodes}")
        print("Path: " + " → ".join(map(str, path)))
    else:
        print("No path found.")