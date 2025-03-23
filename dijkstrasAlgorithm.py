import heapq
from parse import parse_file

filename = "PathFinder-test.txt"
nodes, edges, origin, destinations = parse_file(filename)
# Minheap begins on node 2 (1 according to arr)
minHeap = [(0, 2 - 1)]
visited = set()

while minHeap:
    weight, node = heapq.heappop(minHeap)
    if any(node == destination for destination in destinations):
        print("Got to destination " + str(node) + " in " + str(weight))
        break
    if node in visited:
        continue
    print("On node " + str(node))
    visited.add(node)
    for edge in edges[node]:
        if edge[0] not in visited:
            heapq.heappush(minHeap, (edge[1] + weight, edge[0]))
            print("Pushed " + str(edge[0]))