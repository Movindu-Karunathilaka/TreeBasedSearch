import sys
import heapq

# ! Still needs to implement parsing !

nodes = [(4,1), (2,2), (4,4), (6,3), (5,6), (7,5)]
destinations = [4, 3]

# Node value deducted by one for arr reference (e.g. node 2 is indicated as 1 in the arr)
edgesRaw = [(2,1,4), (3,1,5), (1,3,5), (2,3,4), (3,2,5), (4,1,6), (1,4,6), (4,3,5), (3,5,6), (5,3,6), (4,5,7), (5,4,8), (6,3,7), (3,6,7)]
edges = {}
for edge in edgesRaw:
    if edge[0] - 1 not in edges:
        edges[edge[0] - 1] = []
    edges[edge[0] - 1].append((edge[1] - 1, edge[2]))

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