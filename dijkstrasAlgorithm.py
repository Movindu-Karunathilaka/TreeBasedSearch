import heapq
from parse import parse_file

filename = "PathFinder-test.txt"
nodes, edges, origin, destinations = parse_file(filename)
# Minheap begins on node 2 (1 according to arr)
minHeap = [(0, 2 - 1)]
visited = set()

while minHeap:
    weight, node = heapq.heappop(minHeap)
    if node in visited:
        print(f"Node {node} already visited")
        continue
    print(f"\nCurrently:\nAt node {node + 1} with current distance {weight}")
    if any(node == destination for destination in destinations):
        print(f"\nFinished\nGot to destination {node + 1} in {weight}.")
        break
    visited.add(node)
    print("Adding node edges:")
    for edge in edges[node]:
        if edge[0] not in visited:
            heapq.heappush(minHeap, (edge[1] + weight, edge[0]))
            print(f"Pushed node {edge[0] + 1} with distance {edge[1] + weight}.")
        else:
            print(f"Node {edge[0] + 1} has already been visited.")
    print("Priority Queue Size:")
    for value in minHeap:
        print(f"Node: {value[1]} Size: {value[0]}")